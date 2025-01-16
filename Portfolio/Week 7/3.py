"""
Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on.
"""
#dictionary to store countries and capitals
countries_capitals = {}

def manage_countries_and_capitals():
    while True:
        country = input("Enter the name of a country (or type 'exit' to quit): ").lower()
        
        if country == 'exit':
            print("Exiting the program.")
            break
        
        if country in countries_capitals:
            print(f"The capital of {country.capitalize()} is {countries_capitals[country].capitalize()}.")
        else:
            capital = input(f"I don't know the capital of {country.capitalize()}. Please enter it: ")
            countries_capitals[country] = capital
            print(f"The capital of {country.capitalize()} is {capital.capitalize()}.")

manage_countries_and_capitals()