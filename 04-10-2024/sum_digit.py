

def sum_digit(number):
    number = abs(number)  # Ensure the number is positive to handle negatives
    sum_digits = 0

    while number > 0:
        sum_digits += number % 10  
        number //= 10  

    print(sum_digits)  
        
sum_digit(-121453)        