# Convert celcius into Fahrenheit. F = (9/5 * C) + 32
def farh():
    cel = int(input("enter cel :"))

    print(f"{cel} celcius in farhenheit is {((9/5)*cel) + 32}")

farh()