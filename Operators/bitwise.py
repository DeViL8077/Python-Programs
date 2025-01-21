# Define two numbers
a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Bitwise AND
result_and = a & b  # 1010 & 0100 = 0000 (Decimal: 0)
print("Bitwise AND:", result_and)

# Bitwise OR
result_or = a | b   # 1010 | 0100 = 1110 (Decimal: 14)
print("Bitwise OR:", result_or)

# Bitwise XOR
result_xor = a ^ b  # 1010 ^ 0100 = 1110 (Decimal: 14)
print("Bitwise XOR:", result_xor)

# Bitwise NOT
result_not = ~a     # ~1010 = -(1010 + 1) = -11 (Two's complement)
print("Bitwise NOT:", result_not)

# Bitwise Left Shift
result_lshift = a << 2  # 1010 << 2 = 101000 (Decimal: 40)
print("Left Shift:", result_lshift)

# Bitwise Right Shift
result_rshift = a >> 2  # 1010 >> 2 = 0010 (Decimal: 2)
print("Right Shift:", result_rshift)
