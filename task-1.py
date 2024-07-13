import argparse
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser(description="Image sorting")
    parser.add_argument(
        "-S", "--source", type=Path, required=True, help="Images directory"
    )
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("output"),
        help="Sorted images directory",
    )
    return parser.parse_args()


def recursive_copy(src: Path, dst: Path):
    if not src.is_dir():
        raise NotADirectoryError(
            f"Source '{src}' is not a directory or does not exist."
        )

    print(f"Copying from {src} to {dst}")

    try:
        for item in src.iterdir():
            if item.is_dir():
                recursive_copy(item, dst / item.name)
            else:
                file_extension = item.suffix.lower()[1:]  # .jpg -> jpg
                folder = dst / file_extension
                folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, folder)
                print(f"Copied {item} to {folder}")
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred during copying: {e}")


def main():
    args = parse_argv()
    print(f"Arguments: source={args.source}, output={args.output}")

    # Check if the source directory exists
    if not args.source.is_dir():
        print(
            f"Error: Source path '{args.source}' is not a directory or does not exist."
        )
        return

    # Create the output directory if it doesn't exist
    if not args.output.exists():
        args.output.mkdir(parents=True, exist_ok=True)

    try:
        recursive_copy(args.source, args.output)
    except Exception as e:
        print(f"An error occurred during copying: {e}")


if __name__ == "__main__":
    main()
