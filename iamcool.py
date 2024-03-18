number = int(input("Enter the number for which you want the multiplication table: "))
limit = int(input("Enter the limit for the multiplication table: "))
print(f"Multiplication table for {number} up to {limit}:")
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")
