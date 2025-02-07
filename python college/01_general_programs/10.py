# Convert dollars into pound where 1 $ = 48 Rs. And 1 pound = 70 Rs.
def pound():
    doll = int(input("enter dollars:"))

    print(f"{doll} dollars in pound is {doll*(48/70)}")

pound()