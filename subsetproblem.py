def visualize_subset_sum(numbers, target):
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

# Example usage
numbers = [2, 4, 6, 8, 10]
target = 16
visualize_subset_sum(numbers, target)
