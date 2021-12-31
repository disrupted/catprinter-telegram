import subprocess
from pathlib import Path


def print_image(path: Path):
    try:
        subprocess.run(f"python catprinter/print.py {path}".split())
    finally:
        # delete image
        path.unlink()
