while True:
    print("\n===== SHOPPING MALL BILL COUNTER =====")
    print("1. Add Item")
    print("2. Make Bill")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))

        f = open("items.txt", "a")
        f.write(item + "," + str(price) + "\n")
        f.close()

        print("Item added successfully!")

    elif choice == "2":
        items = {}

        f = open("items.txt", "r")
        for line in f:
            name, price = line.strip().split(",")
            items[name] = float(price)
        f.close()

        n = int(input("How many items are there? "))

        total = 0

        print("\n--------- BILL ---------")

        for i in range(n):
            item = input(f"Enter item {i+1} name: ")

            if item in items:
                print(item, "=", items[item])
                total += items[item]
            else:
                print(item, "= Item not found")

        print("------------------------")
        print("Total Amount =", total)
        print("------------------------")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")
