print("***********WELCOME MY HOTEL***********")

print("....Breakfast....")

print("1.dhosa     40""\n""2.idly(2)   15""\n""3.pongal    40""\n""4.poori(2)  30""\n")

menus=("dhosa","idly","pongal","poori")

your_order=input("enter your order : ")

dhosa=40
idly=15
pongal=40
poori=30

if your_order in menus:
    print(f"{your_order} is available ")
    how_many=int(input(f"how many {your_order} you want :"))
    
    if your_order == "dhosa":
        total=dhosa*how_many
        print(f"your bill is {total}")

    elif your_order == "idly":
        total=idly*how_many
        print(f"your bill is {total}")

    elif your_order == "pongal":
        total=pongal*how_many
        print(f"your bill is {total}")

    elif your_order == "poori":
        total=poori*how_many
        print(f"your bill is {total}")

else:
    print(f"sorry {your_order} is not available")
