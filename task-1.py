from pathlib import Path
import shutil
import argparse

COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[91m"


def copy_and_sort_files(source_dir, dest_dir="dist"):

    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)

    if not source_dir.exists():
        print(f"{COLOR_BLUE}Вихідна директорія не існує!{COLOR_RESET}")
        return

    if not dest_dir.exists():
        try:
            dest_dir.mkdir()
        except Exception as e:
            print(
                f"{COLOR_RED}Не вдалося створити директорію призначення: {e}{COLOR_RESET}"
            )
            return

    for item in source_dir.iterdir():
        try:
            if item.is_dir():
                copy_and_sort_files(item, dest_dir)
            elif item.is_file():

                extension = item.suffix[1:]
                dest_subdir = dest_dir / extension
                dest_subdir.mkdir(exist_ok=True)
                shutil.copy2(item, dest_subdir)
        except Exception as e:
            print(f"{COLOR_RED}Не вдалося обробити {item}: {e}{COLOR_RESET}")


def main():
    parser = argparse.ArgumentParser(
        description="Копіювання файлів з сортуванням за розширенням."
    )

    parser.add_argument("src", type=Path, help="Шлях до вихідної директорії")

    parser.add_argument(
        "dest",
        type=Path,
        nargs="?",
        default="dist",
        help='Шлях до директорії призначення (за замовчуванням "dist")',
    )

    args = parser.parse_args()

    if not args.src.is_dir():
        print(f"Помилка: Директорія {args.src} не існує або не є директорією.")
        return

    try:
        args.dest.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(
            f"{COLOR_RED}Не вдалося створити директорію призначення: {e}{COLOR_RESET}"
        )
        return
    copy_and_sort_files(args.src, args.dest)
    print(f"Файли успішно скопійовані до {args.dest}")


if __name__ == "__main__":
    main()
