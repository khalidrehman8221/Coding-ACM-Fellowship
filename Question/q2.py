num = int(input("Enter the number: "))

sum = 0
current_number = 1

while num > 0:
    sum += current_number
    current_number += 1
    num -= 1

print("The sum of first", num, "positive is" ,sum )