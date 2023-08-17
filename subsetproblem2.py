import matplotlib.pyplot as plt
import time

def visualize_subset_sum(numbers, target):
    plt.figure(figsize=(10, 5))
    plt.title("Subset Sum Backtracking Visualization")
    plt.xlabel("Index")
    plt.ylabel("Current Sum")
    
    def subset_sum_recursive(numbers, target, current_sum, index, subset):
        plt.scatter(index, current_sum, color='blue')
        plt.pause(0.1)  # Pause to visualize
        
        if current_sum == target:
            print("Solution found:", subset)
            return
        
        if index >= len(numbers) or current_sum > target:
            plt.scatter(index, current_sum, color='red')
            plt.pause(0.1)  # Pause to visualize
            return
        
        # Include the current number in the subset
        subset_sum_recursive(numbers, target, current_sum + numbers[index], index + 1, subset + [numbers[index]])
        
        # Exclude the current number from the subset
        subset_sum_recursive(numbers, target, current_sum, index + 1, subset)
    
    subset_sum_recursive(numbers, target, 0, 0, [])
    
    plt.show()

# Example usage
numbers = [2, 4, 6, 8, 10]
target = 16
visualize_subset_sum(numbers, target)
