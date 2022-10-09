print("wellcome To Python Pizza Delivey! ")
size = input ("what size pizza do you want? S, M, L\n ")
add_pepperoni = input("do you want pepperoni? Y, N\n  ")
extra_cheese = input("Do you want extra cheese? Y, N\n  ")

bill = 0

if  size == "S":
    bill += 15
elif size == "M":
        bill += 20
elif size == "L":
        bill += 25

if add_pepperoni == "Y":
        if size == "S":
                bill += 2
        else:
                bill += 3
if extra_cheese == "Y":
        bill += 1
print(f"your final bill is ${bill}")
