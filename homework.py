height = 7
width = 2 * height - 1  
for i in range(height):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))
for _ in range(2):
    print(" " * (height - 2) + "***")
print("*" * width)