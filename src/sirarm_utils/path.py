import glob
import re
from pathlib import Path


def increment_path(path, sep='', mkdir=False, increment=True):
    path = Path(path)  # os-agnostic
    if path.exists() and increment:
        suffix = path.suffix
        path = path.with_suffix('')
        dirs = glob.glob(f"{path}{sep}*")  # similar paths
        matches = [re.search(rf"%s{sep}(\d+)" % path.stem, d) for d in dirs]
        i = [int(m.groups()[0]) for m in matches if m]  # indices
        n = max(i) + 1 if i else 2
        path = Path(f"{path}{sep}{n}{suffix}")
    if mkdir:
        path.mkdir(parents=True, exist_ok=True)  # make dir
    return path
