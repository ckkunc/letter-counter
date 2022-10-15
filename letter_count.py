"""Count the letters used by a .txt file"""

from typing import Dict, List
from matplotlib import pyplot
import os


def main() -> None:
    """Entrypoint to our program"""
    path: str = input("Please input the path of your file: ")
    if os.path.exists(path):
        letter_counts = read_character_data(path)
        chart_data(letter_counts)
    else: 
        print("Please input the file location correctly")
        print(path)
        choice: str = input("Type 'yes' to retry, 'no' to quit: ")
        if choice == True:
                main()
        else: 
                quit()


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
    """Plot the results of our textual analysis"""
    pyplot.title("Counts of Letters")
    pyplot.xlabel("Letters")
    pyplot.ylabel("Count")
    labels: List[str] = list(letter_counts.keys())
    values: List[int] = list(letter_counts.values())
    pyplot.bar(labels, values)
    pyplot.show()

    
if __name__ == "__main__":
    main()
