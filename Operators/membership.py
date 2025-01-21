# Example 1: Using 'in' with a list
fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)   # True, 'apple' is in the list
print('grape' in fruits)   # False, 'grape' is not in the list

# Example 2: Using 'not in' with a string
text = "Hello, World!"
print('Hello' in text)     # True, 'Hello' is in the string
print('hello' in text)     # False, case-sensitive check
print('Python' not in text)  # True, 'Python' is not in the string

# Example 3: Using 'in' with a dictionary (checks keys)
my_dict = {'a': 1, 'b': 2, 'c': 3}
print('a' in my_dict)      # True, 'a' is a key in the dictionary
print(1 in my_dict)        # False, 1 is not a key (values are not checked)

# Example 4: Using 'in' with a set
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)        # True, 3 is in the set
print(10 not in numbers)   # True, 10 is not in the set
