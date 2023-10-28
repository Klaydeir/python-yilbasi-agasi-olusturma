height = int(input("Yılbaşı Ağacı'nın Uzunluğu: "))

for i in range(int(height * 0.5)):
    print(" " * (height - i) + "*" * (2 * i + 1))
    
for i in range(int(height * 0.5)):
    print((" " * (height - 1)) + "||")
