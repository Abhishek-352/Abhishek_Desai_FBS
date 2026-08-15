# And(&)
x = 5
y = 3
print(x & y)  # 1, because 5 in binary is 101 and 3 in binary is 011, so 101 & 011 = 001


# Or(|)
x = 5
y = 3
print(x | y)  # 7, because 5 in binary is 101 and 3 in binary is 011, so 101 | 011 = 111


# Xor(^)    
x = 5
y = 3
print(x ^ y)  # 6, because 5 in binary is 101 and 3 in binary is 011, so 101 ^ 011 = 110


# Not(~)
x = 5
print(~x)  # -6, because ~5 in binary is -110 (two's complement representation)


# Left Shift(<<)
x = 5
print(x << 1)  # 10, because shifting 5 (101 in binary) left by 1 bit gives 1010 (10 in decimal)


# Right Shift(>>)
x = 5
print(x >> 1)  # 2, because shifting 5 (101 in binary) right by 1 bit gives 10 (2 in decimal)
