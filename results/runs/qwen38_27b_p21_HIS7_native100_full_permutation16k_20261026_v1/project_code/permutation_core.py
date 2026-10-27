"""Exact full-permutation prefix language for independently frozen native T3 IDs.

Every ordering of every supplied candidate remains possible. Only JSON spelling
is canonicalized; no target score, model weight or saved output is read.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"
CONDITION = "PFARENA_T3_REVIEWED_MAMMAL_DOMAIN_FULL_PERMUTATION_V1"
SPACE = b" \t\n\r"
HEADER = b'{"ranking":['


class ConstraintError(ValueError):
    pass


@dataclass(frozen=True)
class State:
    phase: str = "header"
    header_index: int = 0
    fragment: str = ""
    used: frozenset[str] = frozenset()


class UniquePermutationLanguage:
    def __init__(self, candidate_ids: list[str]):
        from input_contract import mutation_parts
        if (not isinstance(candidate_ids, list) or not candidate_ids or len(candidate_ids) > 1000
                or any(not isinstance(x, str) for x in candidate_ids)
                or len(set(candidate_ids)) != len(candidate_ids)):
            raise ConstraintError("complete_unique_candidate_list_required")
        for value in candidate_ids:
            mutation_parts(value)
        self.allowed = frozenset(candidate_ids)
        self.count = len(candidate_ids)
        prefixes: dict[str, set[str]] = {}
        for mutation in self.allowed:
            for length in range(1, len(mutation) + 1):
                prefixes.setdefault(mutation[:length], set()).add(mutation)
        self.by_prefix = {k: frozenset(v) for k, v in prefixes.items()}

    def step(self, state: State, byte: int) -> State:
        char = chr(byte)
        phase = state.phase
        if phase == "header":
            # Whitespace outside the exact property-name string is permitted.
            if byte in SPACE and state.header_index in {0, 1, 10, 11}:
                return state
            if byte != HEADER[state.header_index]:
                raise ConstraintError("unexpected_JSON_header_byte")
            index = state.header_index + 1
            return State("value" if index == len(HEADER) else "header", index, "", state.used)
        if phase == "string":
            if byte == ord('"'):
                if state.fragment not in self.allowed or state.fragment in state.used:
                    raise ConstraintError("invalid_or_repeated_mutation")
                return State("separator", 0, "", state.used | {state.fragment})
            fragment = state.fragment + char
            candidates = self.by_prefix.get(fragment)
            if not candidates or not candidates - state.used:
                raise ConstraintError("no_unused_input_valid_ID_has_this_prefix")
            return State("string", 0, fragment, state.used)
        if byte in SPACE:
            return state
        if phase == "value":
            if byte != ord('"') or len(state.used) >= self.count:
                raise ConstraintError("expected_mutation_string")
            return State("string", 0, "", state.used)
        if phase == "separator":
            expected = ord(']') if len(state.used) == self.count else ord(',')
            if byte != expected:
                raise ConstraintError("ranking_must_have_every_candidate_exactly_once")
            return State("object_end" if len(state.used) == self.count else "value", 0, "", state.used)
        if phase == "object_end":
            if byte != ord('}'):
                raise ConstraintError("unexpected_object_member_or_closing_byte")
            return State("done", 0, "", state.used)
        raise ConstraintError("bytes_after_complete_JSON")

    def feed(self, state: State, data: bytes) -> State:
        for byte in data:
            state = self.step(state, byte)
        return state


def bytelevel_inverse() -> dict[str, int]:
    # Exact GPT2/ByteLevel byte alphabet. The CPU checkpoint test independently
    # compares every usable piece against the pinned Tokenizers decoder.
    direct = list(range(ord('!'), ord('~') + 1)) + list(range(161, 173)) + list(range(174, 256))
    chars = direct.copy(); next_codepoint = 256
    for byte in range(256):
        if byte not in direct:
            direct.append(byte); chars.append(next_codepoint); next_codepoint += 1
    return {chr(codepoint): byte for byte, codepoint in zip(direct, chars)}


class TokenVocabulary:
    """Exact ASCII token-byte trie; irrelevant/invalid/special tokens are masked."""
    def __init__(self, pieces: dict[int, bytes], eos_ids: set[int], vocab_size: int):
        self.pieces = pieces
        self.eos_ids = frozenset(eos_ids)
        self.vocab_size = vocab_size
        self.trie: dict = {}
        for token_id, piece in pieces.items():
            if not piece or token_id in self.eos_ids:
                raise ConstraintError("empty_or_EOS_piece_in_ordinary_vocabulary")
            node = self.trie
            for byte in piece:
                node = node.setdefault(byte, {})
            node.setdefault(None, []).append(token_id)

    @classmethod
    def from_checkpoint_tokenizer(cls, path: Path, expected_sha256: str, eos_ids: set[int]):
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected_sha256:
            raise ConstraintError("checkpoint_tokenizer_hash_mismatch")
        config = json.loads(raw)
        decoder = config.get("decoder", {})
        if decoder.get("type") != "ByteLevel" or decoder.get("add_prefix_space") is not False:
            raise ConstraintError("unsupported_nonliteral_ByteLevel_decoder")
        if config.get("model", {}).get("type") != "BPE":
            raise ConstraintError("unsupported_tokenizer_model")
        inverse = bytelevel_inverse()
        special = {x["id"] for x in config.get("added_tokens", []) if x.get("special")}
        if not eos_ids or not eos_ids <= special:
            raise ConstraintError("EOS_must_be_explicit_checkpoint_special_tokens")
        # Ordinary added tokens are excluded deliberately: the base BPE byte
        # alphabet already represents every accepted character and ranking.
        pieces = {}
        alphabet = set(b'{}[]":,ranking0123456789 \t\r\n' + AMINO_ACIDS.encode() + b'+')
        vocab = config["model"]["vocab"]
        for text, token_id in vocab.items():
            if token_id in special:
                continue
            try:
                piece = bytes(inverse[c] for c in text)
            except KeyError:
                raise ConstraintError("unexpected_BPE_byte_alphabet")
            if piece and set(piece) <= alphabet:
                pieces[token_id] = piece
        full_size = max([*vocab.values(), *(x["id"] for x in config.get("added_tokens", []))]) + 1
        return cls(pieces, eos_ids, full_size)

    def allowed_next_ids(self, language: UniquePermutationLanguage, state: State) -> list[int]:
        result = list(self.eos_ids) if state.phase == "done" else []
        stack = [(self.trie, state)]
        while stack:
            node, prefix_state = stack.pop()
            result.extend(node.get(None, ()))
            for byte, child in node.items():
                if byte is None:
                    continue
                try:
                    following = language.step(prefix_state, byte)
                except ConstraintError:
                    continue
                stack.append((child, following))
        return result


class RequestConstraint:
    """Single-pass no-backtracking output-prefix state used by the vLLM adapter."""
    def __init__(self, candidate_ids: list[str], vocabulary: TokenVocabulary):
        self.language = UniquePermutationLanguage(candidate_ids)
        self.vocabulary = vocabulary
        self.state = State()
        self.output_ids: list[int] = []
        self.eos_seen = False

    def update(self, output_ids: list[int]) -> None:
        if output_ids[:len(self.output_ids)] != self.output_ids:
            raise ConstraintError("output_history_rewrite_or_speculation_not_supported")
        for token_id in output_ids[len(self.output_ids):]:
            if self.eos_seen:
                # The pinned legacy asynchronous engine can retain an already
                # finished row through late sampling callbacks. Only repeated
                # internal EOS is legal in that absorbing terminal state.
                if token_id not in self.vocabulary.eos_ids:
                    raise ConstraintError("ordinary_tokens_after_EOS")
                continue
            if token_id in self.vocabulary.eos_ids:
                if self.state.phase != "done":
                    raise ConstraintError("premature_EOS")
                self.eos_seen = True
            else:
                piece = self.vocabulary.pieces.get(token_id)
                if piece is None:
                    raise ConstraintError("invalid_or_special_token_generated")
                self.state = self.language.feed(self.state, piece)
        self.output_ids = list(output_ids)

    def __call__(self, output_ids, logits):
        import torch

        self.update(output_ids)
        if self.eos_seen:
            if self.state.phase != "done" or len(self.state.used) != self.language.count:
                raise ConstraintError("EOS_without_complete_full_permutation_state")
            # Do not consult a terminated upstream grammar's all-inf mask.
            # The response is already complete and EOS-confirmed: make this
            # internal row EOS-only and finite until the scheduler retires it.
            # No ordinary token or new mutation can be emitted here.
            indices = torch.tensor(sorted(self.vocabulary.eos_ids), dtype=torch.long, device=logits.device)
            if int(indices.max()) >= logits.shape[-1]:
                raise ConstraintError("wrong_model_vocabulary_at_terminal_EOS")
            logits.fill_(float("-inf"))
            logits.index_fill_(0, indices, 0.0)
            return logits
        allowed = self.vocabulary.allowed_next_ids(self.language, self.state)
        if not allowed or max(allowed) >= logits.shape[-1]:
            raise ConstraintError("empty_constraint_or_wrong_model_vocabulary")
        indices = torch.tensor(allowed, dtype=torch.long, device=logits.device)
        kept = logits.index_select(0, indices)
        if not bool(torch.isfinite(kept).any()):
            raise ConstraintError("no_finite_allowed_logit_no_unconstrained_fallback")
        logits.fill_(float("-inf"))
        logits.index_copy_(0, indices, kept)
        return logits
