print("Newton's Second Law of Moton")

#Determining the missing value 
print("Select the missing value:")
print("1. Mass(m)")
print("2. Acceleration(a)")
print("3. Force(F")

mvc = input("Enter the option number for the missing value:")

if mvc == "1":
    a = float(input("Enter acceleration (a):"))
    F = float(input("Enter force (F):"))
    m = F / a 
    print(f"Mass (m) = {m}")

elif mvc == "2":
    m = float(input("Enter mass (m):"))
    F = float(input("Enter force (F):" ))
    a = F / m 
    print(f"Acceleration (a) = {a}")

elif mvc == "3":
    m = float(input("Enter mass(m):"))
    a = float(input("Enter acceleration (a):"))
    F = m * a 
    print(f"Force (F) = {F}")

else:
    print("Invalid ccc.")
