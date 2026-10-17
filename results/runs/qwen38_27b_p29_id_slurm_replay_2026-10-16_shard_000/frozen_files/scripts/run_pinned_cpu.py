"""Run only a hash-frozen CPU command in the pinned portable scoring runtime."""
import hashlib,json,os,subprocess,sys,tarfile,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=Path('/dfs/scratch0/dongweij/bio-evaluation/.local/remaining_evaluations/scoring_runtime/scoring-runtime-py310.tar.gz')
ARCHIVE_SHA='f7de6fa792551aadac025004b02227d074b50af0dfcd52c1ea50eeaa7c7c1742'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while chunk:=f.read(8*1024*1024):h.update(chunk)
 return h.hexdigest()
if len(sys.argv)<2:raise SystemExit('Expected a frozen relative CPU script path')
name=sys.argv[1];target=(ROOT/name).resolve()
allowed=json.loads((ROOT/'configs/cpu_commands.json').read_text())
if name not in allowed or not target.is_relative_to(ROOT/'scripts') or sha(target)!=allowed[name]:
 raise ValueError('CPU command is not hash-frozen inside this project')
if sha(ARCHIVE)!=ARCHIVE_SHA:raise ValueError('Portable scoring runtime archive changed')
with tempfile.TemporaryDirectory(prefix='bio-pinned-score-',dir=os.environ.get('SLURM_TMPDIR','/tmp')) as folder:
 with tarfile.open(ARCHIVE) as source:source.extractall(folder,filter='data')
 result=subprocess.run([str(Path(folder)/'score_python.sh'),str(target),*sys.argv[2:]],cwd=ROOT)
 raise SystemExit(result.returncode)
