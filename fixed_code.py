
def calculate_average(numbers):
    """Calculate the average of a non-empty list."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")

    return sum(numbers) / len(numbers)


def main():
    values = [10, 20, 30]
    print("Average:", calculate_average(values))


if __name__ == "__main__":
    main()
