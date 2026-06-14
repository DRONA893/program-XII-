
from reportlab.pdfgen import canvas
from datetime import datetime
import os

ITEMS_FILE = "items.txt"
BILLNO_FILE = "billno.txt"
BILLS_FOLDER = "Bills"

# Create Bills folder automatically
if not os.path.exists(BILLS_FOLDER):
    os.makedirs(BILLS_FOLDER)


# -----------------------------
# BILL NUMBER FUNCTION
# -----------------------------
def get_bill_number():

    try:
        f = open(BILLNO_FILE, "r")
        bill_no = int(f.read())
        f.close()

    except:
        bill_no = 1

    f = open(BILLNO_FILE, "w")
    f.write(str(bill_no + 1))
    f.close()

    return bill_no


# -----------------------------
# LOAD ITEMS
# -----------------------------
def load_items():

    items = {}

    try:

        f = open(ITEMS_FILE, "r")

        for line in f:

            data = line.strip().split(",")

            if len(data) == 3:

                name = data[0].lower()
                price = float(data[1])
                unit = data[2].lower()

                items[name] = (price, unit)

        f.close()

    except FileNotFoundError:

        print("items.txt not found!")

    return items


# -----------------------------
# ADD ITEM
# -----------------------------
def add_item():

    print("\nADD NEW ITEM")

    name = input("Enter item name: ").lower()

    try:
        price = float(input("Enter price: "))
    except:
        print("Invalid price")
        return

    unit = input("Enter unit (kg/piece): ").lower()

    if unit not in ["kg", "piece"]:

        print("Unit must be kg or piece")
        return

    f = open(ITEMS_FILE, "a")

    f.write(name + "," + str(price) + "," + unit + "\n")

    f.close()

    print("Item added successfully!")


# -----------------------------
# REMOVE ITEM
# -----------------------------
def remove_item():

    item_name = input(
        "Enter item name to remove: "
    ).lower()

    try:

        f = open(ITEMS_FILE, "r")

        lines = f.readlines()

        f.close()

        found = False

        f = open(ITEMS_FILE, "w")

        for line in lines:

            if not line.lower().startswith(
                item_name + ","
            ):

                f.write(line)

            else:

                found = True

        f.close()

        if found:

            print("Item removed successfully!")

        else:

            print("Item not found!")

    except:

        print("Error removing item")


# -----------------------------
# VIEW ITEMS
# -----------------------------
def view_items():

    items = load_items()

    if len(items) == 0:

        print("No items found")
        return

    print("\nAVAILABLE ITEMS")
    print("-" * 60)

    for name, value in items.items():

        price = value[0]
        unit = value[1]

        print(
            f"{name:<30} Rs.{price:<10} per {unit}"
        )

# -----------------------------
# MAKE BILL
# -----------------------------
def make_bill():

    items = load_items()

    if len(items) == 0:

        print("No items available!")
        return

    try:
        n = int(
            input("How many items in bill? ")
        )

    except:

        print("Invalid number")
        return

    bill_no = get_bill_number()

    now = datetime.now()

    total = 0

    bill_lines = []

    bill_lines.append(
        "SHOPPING MALL BILL"
    )

    bill_lines.append(
        "Bill No : " + str(bill_no)
    )

    bill_lines.append(
        now.strftime("%d-%m-%Y %H:%M:%S")
    )

    bill_lines.append(
        "-" * 40
    )

    print("\n----------- BILL -----------")

    for i in range(n):

        item = input(
            f"Enter item {i+1} name: "
        ).lower()

        if item not in items:

            print("Item not found")

            bill_lines.append(
                item + " = Item not found"
            )

            continue

        price = items[item][0]
        unit = items[item][1]

        if unit == "kg":

            grams = float(
                input(
                    "Enter quantity in grams: "
                )
            )

            amount = (
                grams / 1000
            ) * price

            print(
                item,
                grams,
                "g = Rs.",
                round(amount, 2)
            )

            bill_lines.append(
                f"{item} {grams:.0f}g = Rs.{amount:.2f}"
            )

        else:

            pieces = int(
                input(
                    "Enter quantity in pieces: "
                )
            )

            amount = (
                pieces * price
            )

            print(
                item,
                "x",
                pieces,
                "= Rs.",
                round(amount, 2)
            )

            bill_lines.append(
                f"{item} x{pieces} = Rs.{amount:.2f}"
            )

        total += amount

    bill_lines.append(
        "-" * 40
    )

    bill_lines.append(
        f"TOTAL = Rs.{total:.2f}"
    )

    bill_lines.append(
        "-" * 40
    )

    bill_lines.append(
        "Thank You Visit Again"
    )

    print(
        "\nTotal Amount = Rs.",
        round(total, 2)
    )

    filename = os.path.join(
        BILLS_FOLDER,
        f"bill_{bill_no}.pdf"
    )

    pdf = canvas.Canvas(filename)

    y = 800

    for line in bill_lines:

        pdf.drawString(
            50,
            y,
            line
        )

        y -= 20

    pdf.save()

    print(
        "\nBill saved as:",
        filename
    )

    try:

        os.startfile(filename)

    except:

        pass

    try:

        os.startfile(
            filename,
            "print"
        )

        print(
            "Bill sent to printer."
        )

    except:

        print(
            "Printer not connected."
        )


# -----------------------------
# INTRODUCTION
# -----------------------------
print("=" * 50)
print("SHOPPING MALL BILLING SYSTEM")
print("=" * 50)
print("Features:")
print("1. Add Item")
print("2. Remove Item")
print("3. View Items")
print("4. Make Bill")
print("5. Exit")
print()
print("Prices are stored per KG")
print("or per PIECE.")
print("Bills are saved as PDF.")
print("=" * 50)


# -----------------------------
# MAIN MENU
# -----------------------------
while True:

    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Make Bill")
    print("5. Exit")

    choice = input(
        "Enter your choice: "
    )

    if choice == "1":

        add_item()

    elif choice == "2":

        remove_item()

    elif choice == "3":

        view_items()

    elif choice == "4":

        make_bill()

    elif choice == "5":

        print(
            "Thank you for using the system!"
        )

        break

    else:

        print(
            "Invalid Choice"
        )
