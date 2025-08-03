grocery= ["Milk", "Bread", "Pulses"]
while True:
    new = input("Enter your grocery item: ")
    if new in grocery:
        print("Entered successfully")
        break
    else:
        grocery.append(new)
        print(f"{new}")
        print("\nGrocery List:")
        for item in grocery:
            print("-", item)