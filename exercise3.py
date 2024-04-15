def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement
    return arr

def main():
    # Step 1: Prompt user to input an array of integers
    input_array = input("Enter an array of integers separated by spaces: ")
    arr = list(map(int, input_array.split()))

    # Step 2: Implement quick sort algorithm
    sorted_arr = quick_sort(arr[:])

    # Step 3: Display the sorted array
    print("Sorted array:", sorted_arr)

    # Step 4: Allow user to specify a target element to search for
    target = int(input("Enter the target element to search for: "))

    # Step 5: If target element found, prompt user to input replacement element
    if target in sorted_arr:
        replacement = int(input("Enter the replacement element: "))

        # Step 6: Replace target elements with replacement element
        modified_arr = replace_elements(sorted_arr, target, replacement)

        # Display the modified array
        print("Modified array after replacing elements:", modified_arr)
    else:
        print("Target element not found in the array.")

if __name__ == "__main__":
    main()