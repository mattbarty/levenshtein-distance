import numpy as np


def levenshtein(string1: str, string2: str, *, matrix=False):
    """Levenshtein distance is a string metric for measuring the difference between two sequences.
    Informally, the Levenshtein distance between two words is the minimum number of single-character edits 
    (insertions, deletions or substitutions) required to change one word into the other. 
    ( ~ https://en.wikipedia.org/wiki/Levenshtein_distance)

    Args:
        string1 (str): first word to compare.
        string2 (str): second word to compare.
        matrix (bool, optional): Instead of distance, return a numpy.ndarray object with the complete matrix. Defaults to False.

    Returns:
        distance (int): The "distance" between two words. The minimum number of single-character edits to change one word to another.
    """

    string1 = string1
    string2 = string2
    columns = len(string1) + 1
    rows = len(string2) + 1

    _matrix = np.zeros((rows, columns))

    current_row = [0]  # -- Start at first row (of course)

    for col in range(1, columns):  # -- Populate the first row
        current_row.append(current_row[col - 1] + 1)
        _matrix[0][col] = current_row[-1]

    for row in range(1, rows):
        previous_row = current_row
        current_row = [previous_row[0] + 1]
        _matrix[row][0] = current_row[0]  # -- Populate the first column

        # -- Iterate over the current row and apply Levenshtein logic
        for col in range(1, columns):
            insert_cost = current_row[col - 1] + 1
            delete_cost = previous_row[col] + 1

            if string1[col - 1] != string2[row - 1]:
                replace_cost = previous_row[col - 1] + 1
                _matrix[row][col] = replace_cost
            else:
                replace_cost = previous_row[col - 1]
                _matrix[row][col] = replace_cost

            # -- Populate next element in row
            current_row.append(min(insert_cost, delete_cost, replace_cost))

    if matrix:
        return _matrix
    else:
        return int(_matrix[-1][-1])


if __name__ == '__main__':
    print(levenshtein('matthew', 'tabea'))  # -- Return distance
    print(levenshtein('matthew', 'tabea', matrix=True))  # -- return np.ndarray
