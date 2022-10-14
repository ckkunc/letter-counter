"""Count the letters used by Shakespeare."""

from typing import Dict, List
from matplotlib import pyplot


def main() -> None:
    """Entrypoint to our program"""
    letter_counts = read_character_data("data/shakespeare.txt")
    chart_data(letter_counts)


def read_character_data(file: str) -> Dict[str, int]: 
    """Given a filenam, read its contents and count its characters."""
    counts: Dict[str, int] = {}
    file_handle = open(file, "r")
    for line in file_handle:
        line = line.lower()
        for char in line:
            if char.isalpha():
                if char in counts:
                    counts[char] += 1
                else: 
                    counts[char] = 1
    file_handle.close() 
    return counts


def chart_data(letter_counts: Dict[str, int]) -> None:
    """Plot the results of our textual analysis of Shakespeare"""
    pyplot.title("Counts of Letters in Shakespeare")
    pyplot.xlabel("Letters")
    pyplot.ylabel("Count")
    labels: List[str] = list(letter_counts.keys())
    values: List[int] = list(letter_counts.values())
    pyplot.bar(labels, values)
    pyplot.show()

    
if __name__ == "__main__":
    main()
