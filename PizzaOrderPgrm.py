#Pizza Cost
SmallPizza = 100
MediumPizza = 200
LargePizza = 300
#Cost for Extra Fillings
SmallPepperoni= 30
MediumPepperoni =40
LargePepperoni =50
ExtraCheese = 20

bill = 0

print("Welcome to Pizzeria\n")
print("#Pizza Cost\n Small Pizza (S) = 100\n Medium Pizza (M) = 200\n Large Pizza (L) = 300\n")
print("#Cost for Extra Fillings\n Small Pepperoni= 20\n Medium Pepperoni =40\n Large Pepperoni =50\n Extra Cheese = 20\n")

Pizza = input("Which Pizza do you prefer? ")

if Pizza == "S" or Pizza == "s":
    bill += SmallPizza
    Fillings=input("Do you need any Extra Fillings (Y/N): ")
    if Fillings == "Y" or Fillings ==  "y":
        FillOptions=input("#Filling Options:\n Pepperoni(P), Cheese(C), Both(B)\n")
        if FillOptions=="p"or FillOptions== 'P':
            bill+=SmallPepperoni
            print("\nBill:")
            print(f"\tSmall Pizza\t:\t{SmallPizza}")
            print(f"\tSmall Pepperoni\t:\t{SmallPepperoni}")
            print(f"\tTotal\t\t:\t{bill}")
        elif FillOptions=='c'or FillOptions=='C':
            bill+=ExtraCheese
            print("\nBill:")
            print(f"\tSmall Pizza\t:\t{SmallPizza}")
            print(f"\tExtra Cheese\t:\t{ExtraCheese}")
            print(f"\tTotal\t\t:\t{bill}")
        elif FillOptions=='b' or FillOptions=='B':
            bill+=SmallPepperoni + ExtraCheese
            print("\nBill:")
            print(f"\tSmall Pizza\t:\t{SmallPizza}")
            print(f"\tSmall Pepperoni\t:\t{SmallPepperoni}")
            print(f"\tExtra Cheese\t:\t{ExtraCheese}")
            print(f"\tTotal\t\t:\t{bill}")
    elif Fillings == "N" or Fillings ==  "n":
        print("\nBill:")
        print(f"\tSmall Pizza\t:\t{SmallPizza}")
        print(f"\tTotal\t\t:\t{bill}")
    else:
        pass


elif Pizza == "M" or Pizza == "m":
    bill+=(MediumPizza)
    Fillings=input("Do you need any Extra Fillings (Y/N): ")
    if Fillings == "Y" or Fillings ==  "y":
        FillOptions=input("#Filling Options:\n Pepperoni(P), Cheese(C), Both(B)\n")
        if FillOptions=="p"or FillOptions== 'P':
            bill+=MediumPepperoni
            print("\nBill:")
            print(f"\tMedium Pizza\t:\t{MediumPizza}")
            print(f"\tMedium Pepperoni :\t{MediumPepperoni}")
            print(f"\tTotal\t\t:\t{bill}")
        elif FillOptions=='c'or FillOptions=='C':
            bill+=ExtraCheese
            print("\nBill:")
            print(f"\tMedium Pizza\t:\t{MediumPizza}")
            print(f"\tExtra Cheese\t:\t{ExtraCheese}")
            print(f"\tTotal\t\t:\t{bill}")
        elif FillOptions=='b' or FillOptions=='B':
            bill+=MediumPepperoni + ExtraCheese
            print("\nBill:")
            print(f"\tMedium Pizza\t:\t{MediumPizza}")
            print(f"\tMedium Pepperoni:\t{MediumPepperoni}")
            print(f"\tExtra Cheese\t:\t{ExtraCheese}")
            print(f"\tTotal\t\t:\t{bill}")
    elif Fillings == "N" or Fillings ==  "n":
        print("\nBill:")
        print(f"\tMedium Pizza\t:\t{MediumPizza}")
        print(f"\tTotal\t\t:\t{bill}")
    else:
        pass

elif Pizza == "L" or Pizza == "l":
    bill+=(LargePizza)
    Fillings=input("Do you need any Extra Fillings (Y/N): ")
    if Fillings == "Y" or Fillings ==  "y":
        FillOptions=input("#Filling Options:\n Pepperoni(P), Cheese(C), Both(B)\n")
        if FillOptions=="p"or FillOptions== 'P':
            bill+=LargePepperoni
            print("\nBill:")
            print(f"\tLarge Pizza\t:\t{LargePizza}")
            print(f"\tLarge Pepperoni\t:\t{LargePepperoni}")
            print(f"\tTotal\t\t:\t{bill}")
        elif FillOptions=='c'or FillOptions=='C':
            bill+=ExtraCheese
            print("\nBill:")
            print(f"\tLarge Pizza\t:\t{LargePizza}")
            print(f"\tExtra Cheese\t:\t{ExtraCheese}")
            print(f"\tTotal\t\t:\t{bill}")
        elif FillOptions=='b' or FillOptions=='B':
            bill+=LargePepperoni + ExtraCheese
            print("\nBill:")
            print(f"\tLarge Pizza\t:\t{LargePizza}")
            print(f"\tLarge Pepperoni\t:\t{LargePepperoni}")
            print(f"\tExtra Cheese\t:\t{ExtraCheese}")
            print(f"\tTotal\t\t:\t{bill}")
    elif Fillings == "N" or Fillings ==  "n":
        print("\nBill:")
        print(f"\tLarge Pizza\t:\t{LargePizza}")
        print(f"\tTotal\t\t:\t{bill}")
    else:
        pass