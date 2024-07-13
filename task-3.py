import logging


def hanoi(n, source, target, auxiliary):

    if n == 1:
        logging.info(f"Move disk 1 from {source} to {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        logging.info(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, auxiliary, target, source)


def main():

    try:
        n = int(input("Enter the number of disks: "))
        if n <= 0:
            raise ValueError("The number of disks must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    hanoi(n, "A", "C", "B")
    print("All disks have been moved successfully!")


if __name__ == "__main__":
    main()
