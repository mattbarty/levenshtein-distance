import numpy as np

string1 = 'matilda'
string2 = 'matt'
columns = len(string1) + 1
rows = len(string2) + 1

matrix = np.zeros((rows, columns))

current_row = [0]
for col in range(1, columns):
    current_row.append(current_row[col - 1] + 1)
    matrix[0][col] = current_row[-1]

for row in range(1, rows):
    previous_row = current_row
    current_row = [previous_row[0] + 1]
    matrix[row][0] = current_row[0]

    for col in range(1, columns):
        insert_cost = current_row[col - 1] + 1
        delete_cost = previous_row[col] + 1

        if string1[col - 1] != string2[row - 1]:
            replace_cost = previous_row[col - 1] + 1
            matrix[row][col] = replace_cost
        else:
            replace_cost = previous_row[col - 1]
            matrix[row][col] = replace_cost

        current_row.append(min(insert_cost, delete_cost, replace_cost))