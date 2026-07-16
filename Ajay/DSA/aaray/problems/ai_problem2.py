import numpy as np

marks_matrix = np.array([[
45, 67 ,87], # Student 1 Marks
[34, 56, 85] # Student 2 Marks
])

print(marks_matrix.shape)
print(f'''Student 1 -> Marks:

            Hindi   : {marks_matrix[0, 0]}
            English : {marks_matrix[0, 1]}
            Math    : {marks_matrix[0, 2]}
''')

print(f'''Student 2 -> Marks:

            Hindi   : {marks_matrix[1, 0]}
            English : {marks_matrix[1, 1]}
            Math    : {marks_matrix[1, 2]}
''')

print(f'''Sabse Highest Marks -> {np.max(marks_matrix)}''')
print(f'''Sabse kam Marks -> {np.min(marks_matrix)}''')
print(f'''Avg marks class ki -> {np.mean(marks_matrix)}''')