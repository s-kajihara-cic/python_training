# Read from the User
fav_flavour = "vanilla"  # Satoshi

# Shop
stock1 = "chocolate mint"
stock2 = "vanilla"
stock3 = "coffee"
stock4 = "green tea"

# Expected Output
# Yes, we have vanilla in stock

# Sorry, we ran out strawberry

fav_flavour = input("Please tell me your favorite flavour: ").lower()

# Task 1.1
print("\n-- Task1.1 --")
if fav_flavour == stock1:
    print("Yes, we have chocolate mint in stock")
elif fav_flavour == stock2:
    print("Yes, we have vanilla in stock")
elif fav_flavour == stock3:
    print("Yes, we have coffee in stock")
elif fav_flavour == stock4:
    print("Yes, we have green tea in stock")
else:
    print(f"Sorry, we ran out {fav_flavour}")


# Task 1.2
print("\n-- Task1.2 --")
# has_flavour = False
# if fav_flavour == stock1:
#     has_flavour = True
# elif fav_flavour == stock2:
#     has_flavour = True
# elif fav_flavour == stock3:
#     has_flavour = True
# elif fav_flavour == stock4:
#     has_flavour = True

# if has_flavour:
#     print(f"Yes, we have {fav_flavour} in stock")
# else:
#     print(f"Sorry, we ran out {fav_flavour}")

if (
    fav_flavour == stock1
    or fav_flavour == stock2
    or fav_flavour == stock3
    or fav_flavour == stock4
):
    print(f"Yes, we have {fav_flavour} in stock")
else:
    print(f"Sorry, we ran out {fav_flavour}")


# Task 1.3
stocks = [stock1, stock2, stock3, stock4]
if fav_flavour in stocks:
    print(f"Yes, we have {fav_flavour} in stock")
else:
    print(f"Sorry, we ran out {fav_flavour}")
