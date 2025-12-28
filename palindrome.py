num = int(input("Enter a number: "))
original = num
reverse = 0

for _ in range(len(str(num))):  
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if reverse == original:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
