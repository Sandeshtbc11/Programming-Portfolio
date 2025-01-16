"""
Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).
"""
def factors(num):
    #list to store the factors
    factors = []
  
    # Loop from 1 to the given number
    for i in range(1, num + 1):
        # Check if 'i' divide leaves remainder
        if num % i == 0:
            #If factor, add it to the list
            factors.append(i)
    
    # Print the list of factors
    print(factors)
    
factors(10)

