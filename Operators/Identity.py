# Example 1: Using 'is'
x = [1, 2, 3]
y = x  # y references the same object as x
z = [1, 2, 3]  # z is a different object with the same content

print(x is y)  # True, x and y point to the same object
print(x is z)  # False, x and z point to different objects

# Example 2: Using 'is not'
a = 10
b = 20

print(a is not b)  # True, a and b point to different objects
print(a is b)      # False, a and b are not the same object

# Example 3: Comparing immutable objects
c = 256
d = 256

print(c is d)  # True, Python reuses the same object for small integers
