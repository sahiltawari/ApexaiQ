def count_ways_to_carry_chocolates(n, chocolates, k):
    count = 0  # Initialize count of valid pairs
    
    # Check every pair (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if chocolates[i] + chocolates[j] == k:
                count += 1
                
    return count

def main():
    print("Welcome to Alice's Chocolate Box Selection!\n")
    
    # Read number of test cases
    t = int(input("Enter the number of test cases: "))

    results = []  # List to store results for each test case

    for case_num in range(1, t + 1):
        print(f"\nTest Case {case_num}:")
        
        # Read number of boxes
        n = int(input("Enter the number of boxes: "))
        
        # Read chocolates in each box
        chocolates = list(map(int, input(f"Enter the chocolates in {n} boxes separated by spaces: ").split()))
        
        # Read target sum K
        k = int(input("Enter the required sum of chocolates (K): "))

        # Calculate and store the result
        results.append(count_ways_to_carry_chocolates(n, chocolates, k))

    print("\nResults:")
    for i, res in enumerate(results, 1):
        print(f"Test Case {i}: {res}")

if __name__ == "__main__":
    main()