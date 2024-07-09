def find_min_max(a, b, c):
    
    if a <= b and a <= c:
        minimum = a
    elif b <= a and b <= c:
        minimum = b
    else:
        minimum = c

   
    if a >= b and a >= c:
        maximum = a
    elif b >= a and b >= c:
        maximum = b
    else:
        maximum = c

    return minimum, maximum


if __name__ == "__main__":
    # Input three numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    
    minimum, maximum = find_min_max(num1, num2, num3)

   
    print(f"The minimum number is: {minimum}")
    print(f"The maximum number is: {maximum}")
