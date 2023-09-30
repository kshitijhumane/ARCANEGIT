def is_palindrome(r):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    r = r.replace(" ", "").lower()

    return r == r[::-1]


input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
