import numpy as np

from models.enums import ErrorType


def calculate_weights(matrix):
    # matrix.sum(axis=0) calculates the sum of each column in the matrix.
    # matrix / matrix.sum(axis=0) divides each element in the matrix by the sum of its respective column. This operation scales the values within each column such that the sum of each column becomes 1.
    normalized_matrix = matrix / matrix.sum(axis=0)
    weights_ahp = normalized_matrix.mean(axis=1)  # Calculate the mean along rows
    return weights_ahp


def consistency_index(matrix):
    n = len(matrix)
    eigenvalues, _ = np.linalg.eig(matrix)
    max_eigenvalue = max(abs(eigenvalues))
    consistency_index = (max_eigenvalue - n) / (n - 1)
    random_index = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    random_value = random_index.get(n)
    consistency_ratio = consistency_index / random_value
    return consistency_index, consistency_ratio


v = [1, 1, 2, 2, 1, 1, 2,       # declaration
        1, 1, 1, 1, 1, 1,       # conflict
            1, 1, 1, 1, 1,      # incompatibility
                2, 2, 1, 2,     # assignment
                    1, 1, 1,    # init
                        1, 1,   # params
                            9   # syntax
     ]


pairwise_matrix = [
    [1         , v[0]      , v[1]      , v[2]      , v[3]      , v[4]      , v[5]      , v[6]      ],
    [1 / v[0]  , 1         , v[7]      , v[8]      , v[9]      , v[10]     , v[11]     , v[12]     ],
    [1 / v[1]  , 1 / v[2]  , 1         , v[13]     , v[14]     , v[15]     , v[16]     , v[17]     ],
    [1 / v[3]  , 1 / v[4]  , 1 / v[5]  , 1         , v[18]     , v[19]     , v[20]     , v[21]     ],
    [1 / v[6]  , 1 / v[7]  , 1 / v[8]  , 1 / v[9]  , 1         , v[22]     , v[23]     , v[24]     ],
    [1 / v[10] , 1 / v[11] , 1 / v[12] , 1 / v[13] , 1 / v[14] , 1         , v[25]     , v[26]     ],
    [1 / v[15] , 1 / v[16] , 1 / v[17] , 1 / v[18] , 1 / v[19] , 1 / v[20] , 1         , v[27]     ],
    [1 / v[21] , 1 / v[22] , 1 / v[23] , 1 / v[24] , 1 / v[25] , 1 / v[26] , 1 / v[27] , 1         ]
]

print(pairwise_matrix)


pairwise_matrix = np.array(pairwise_matrix)
# Calculate weights
weights = calculate_weights(pairwise_matrix)
print("Calculated weights:", weights)

# Check consistency
CI, CR = consistency_index(pairwise_matrix)
print(f"Consistency Ratio (CR): {CR}")

if CR < 0.1:  # Adjust the threshold for CR as needed
    print("Consistency is acceptable.")
else:
    print("Inconsistent matrix. Please review the pairwise comparisons.")


for i in range(0, 8):
    print(f"Peso {ErrorType(i)} = {weights[i]}")
