def subset_sum_recursive(numbers, target, current_sum, index, subset):
    if current_sum == target:
        print(subset)
        return
    
    if index >= len(numbers) or current_sum > target:
        return
    
    subset.append(numbers[index])
    subset_sum_recursive(numbers, target, current_sum + numbers[index], index + 1, subset)
    subset.pop()
    
    subset_sum_recursive(numbers, target, current_sum, index + 1, subset)

def subset_sum(numbers, target):
    subset_sum_recursive(numbers, target, 0, 0, [])

# Example usage
numbers = [2, 4, 6, 8, 10]
target = 16
subset_sum(numbers, target)
