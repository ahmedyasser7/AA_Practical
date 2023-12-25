# A Dynamic Programming based Python Program for 0-1 Knapsack problem Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(capacity, weight, value, items):
    # w+1 COLUMNS x n+1 rows table -zeros
    K = [[0 for x in range(capacity + 1)] for x in range(items + 1)]
    # Build table K[][] in bottom up manner
    for i in range(items + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i-1] <= w:
                # if j-wi>=0, j>=wi, wi<=j, wt[i-1] to access thwt in the list correctly since the table contain additional row (0)
                K[i][w] = max(value[i-1] + K[i-1][w-weight[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[items][capacity]


# Driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
