import os

CEG = "\nKavet Hozok Kft.\n"

def print_receipt(items, total_price):
    print("\n----Számla----")
    for item, price in items.items():
        print(f"{item} -------- {price} Ft")
    print(f"\n\nÖsszesen fizetendő: {total_price} Ft\n\n{CEG}\n\n\n")

def get_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input

def main():
    os.system("color 2")
    print("Penztar - \n\n\n")
    while True:
        print("Rendelés megkezdéséhez írd be: new\n")
        new_order = get_input("")
        if new_order.lower() != "new":
            break
        print("\nRendelés megkezdve\n")
        items = {}
        total_price = 0
        print("Termékek:\n-Kávé(parancs: kave )\n-Szállítás(parancs: szallitas )\n\n\n")
        print("Ird be a teteleket: \n")
        while True:
            item = get_input("")
            if item.lower() == "nd":
                break
            elif item.lower() == "kave":
                items["Kávé"] = 50
                total_price += 50
            elif item.lower() == "szallitas":
                items["Szállítás"] = 25
                total_price += 25
            else:
                print("Nem létező termék!")
        print_receipt(items, total_price)
        print("\nRendeles felveve!")
        input("\n\nFolytatáshoz nyomd meg az ENTER-t! >>>")

if __name__ == "__main__":
    main()
