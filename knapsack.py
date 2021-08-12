"""
Find the largest value that can be obtained with total weight < weight_limit
"""

# time: O(weight_limit * total_items)
# space: O(weight_limit * total_items) -> can be reduced to O(weight_limit) using 1 dimensional array.
def knapsack_without_repetitions(weights, values, weight_limit):
    total_items = len(weights)

    # dp[i][j] is the max value that can be obtained using only items 0,..,i and total weight is less than j
    dp = [[0 for smaller_weight_limit in range(weight_limit + 1)] for item_limit in range(total_items)]

    # initialize first row
    for smaller_weight_limit in range(weight_limit + 1):
        if weights[0] <= smaller_weight_limit:
            dp[0][smaller_weight_limit] = values[0]

    # update.
    for item_limit in range(1, total_items):
        for smaller_weight_limit in range(1, weight_limit + 1):
            value_with_new_item = 0
            if weights[item_limit] <= smaller_weight_limit:
                value_with_new_item = dp[item_limit - 1][smaller_weight_limit - weights[item_limit]] + values[
                    item_limit]
            dp[item_limit][smaller_weight_limit] = max(dp[item_limit - 1][smaller_weight_limit], value_with_new_item)

    return dp[total_items - 1][weight_limit]


def knapsack_with_repetitions(weights, values, weight_limit):
    pass

