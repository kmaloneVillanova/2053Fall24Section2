#Folasayo Aiyebo
def sum_list(input_list):
    """
    This function accepts a list of numbers as input and returns the sum of all elements in the list.
    """
    return sum(input_list)

# 
def introduce_person(name, age, city="Unknown"):
    """
    This function accepts a person's name, age, and optionally a city as parameters.
    It returns a formatted string introducing the person.
    """
    return f"My name is {name}, I am {age} years old, and I live in {city}."



# Test cases for sum_list
print(sum_list([1, 2, 3]))         
print(sum_list([10, 20, 30]))      
print(sum_list([-1, -2, -3]))      

# Test cases for introduce_person
print(introduce_person("Alice", 25, "New York"))    
print(introduce_person("Bob", 30))                  
print(introduce_person("Charlie", 22, "Los Angeles"))