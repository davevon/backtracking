import time

def visualize_subset_sum(numbers, target):
    start_time = time.time()

    def subset_sum_recursive(numbers, target, current_sum, index, subset):
        if current_sum == target:
            print("Solution found:", subset)
            return

        if index >= len(numbers) or current_sum > target:
            return

        # Include the current number in the subset
        print(" " * index, "+", numbers[index])
        subset_sum_recursive(numbers, target, current_sum + numbers[index], index + 1, subset + [numbers[index]])

        # Exclude the current number from the subset
        print(" " * index, "-", numbers[index])
        subset_sum_recursive(numbers, target, current_sum, index + 1, subset)

    print("Input set:", numbers)
    print("Target sum:", target)
    print("Exploring subsets...\n")
    subset_sum_recursive(numbers, target, 0, 0, [])

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken:", elapsed_time, "seconds")

# Example usage
numbers = [2, 4, 6, 8, 10]
target = 16
visualize_subset_sum(numbers, target)

############################## Discussion #############################

""" Keep in mind that this backtracking algorithm explores all possible combinations of numbers, which can lead to an exponential time complexity. The time complexity of the backtracking algorithm for the Subset Sum problem is O(2^n), where 'n' is the number of elements in the input set. This is because at each step, the algorithm explores two possibilities: including the current number in the subset or excluding it.

Factors that affect the performance of this algorithm include:

Input Size: As the size of the input set increases, the number of recursive calls and combinations to check grows exponentially, leading to slower performance.
Target Value: If the target value is large, it might take longer to find subsets that add up to it.
Distribution of Numbers: If the numbers in the input set are relatively small and well-distributed, the algorithm might find solutions faster. However, if the numbers are large and closely grouped, the algorithm might take longer due to a larger search space.
Optimization Techniques: There are optimization techniques that can be applied to reduce the search space and improve the performance of the algorithm, like memoization (dynamic programming) to avoid redundant calculations.
In practice, for larger problem instances, more efficient algorithms like dynamic programming can be used to solve the Subset Sum problem with better time complexity. """