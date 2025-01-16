"""
Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers
"""
def prime(num):
    # Check if less than or equal to 1 
    if num <= 1:
        print("Enter a number greater than 1")
    else:
        # Check if the number is divisible by any number between 2 and num-1
        for i in range(2, num):
            if num % i == 0:  
                print("Number is not prime")
                break  
        else:
            print("It's prime")  
            
prime(14)
prime(3)
prime(1)