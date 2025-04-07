def binary_search(arr, target):
    """Performs binary search on a sorted list."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        print(f"Checking index {mid}, value {guess}")

        if guess == target:
            return mid  # Target found
        elif guess < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Target not found

# Sample sorted list
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Input from user
try:
    user_input = int(input("Enter a number to search: "))
    result = binary_search(numbers, user_input)

    if result != -1:
        print(f"✅ Found at index {result}")
    else:
        print("❌ Not found in the list.")
except ValueError:
    print("Please enter a valid integer.")
