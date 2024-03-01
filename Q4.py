def palindrome(word):
    return word == word[::-1]


numbers = [
    "8025833559061079503003059701609553385208",
    "6593036601359343374664733439531066303956",
    "5485839837501070045005400701057389385845",
    "7489617719749244646336564429479177169847"
]

# Check each number and identify the non-palindrome
non_palindromes = [number for number in numbers if not palindrome(number)]

print(non_palindromes)
