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
    try:
        for item in src.iterdir():
            if item.is_dir():
                recursive_copy(item, dst)
            else:
                file_extension = item.suffix.lower()[1:]
                folder = dst / file_extension
                folder.mkdir(parents=True, exist_ok=True)
                dest_file = folder / item.name
                print(f"Copying {item} to {dest_file}")
                shutil.copy2(item, dest_file)
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred: {e}")


def main():
    args = parse_argv()
    print(f"Source: {args.source}, Output: {args.output}")
    if not args.source.exists() or not args.source.is_dir():
        print(
            f"Error: The source directory '{args.source}' does not exist or is not a directory."
        )
        return
    try:
        args.output.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Failed to create output directory: {e}")
        return
    recursive_copy(args.source, args.output)
    print(f"Files successfully copied to {args.output}")


if __name__ == "__main__":
    main()
