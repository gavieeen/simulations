def largest_palindrome(n: int, k: int) -> str:
    # Helper function to check if a number is a palindrome
    def is_palindrome(x: str) -> bool:
        return x == x[::-1]
    # General case: Brute-force check
    high = 10**n - 1
    low = 10**(n - 1)
    for num in range(high, low - 1, -1):
        if num % k == 0 and is_palindrome(str(num)):
            return str(num)
    
    return ''

# Print results for n from 3 to 8 for k values of 4 and 8
for n in range(1, 15):
    print(f"n = {n}, k = 7: {largest_palindrome(n, 8)}")
    # print(f"n = {n}, k = 8: {largest_palindrome(n, 8)}")
