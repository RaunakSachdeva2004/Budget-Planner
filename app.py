n = int(input("Enter a number: "))
if str(n) == str(n)[::-1]:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
