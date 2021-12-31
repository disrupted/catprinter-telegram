from pathlib import Path


def print_image(path: Path):
    try:
        # TODO send image to catprinter
        raise NotImplementedError
    finally:
        # delete image
        path.unlink()
