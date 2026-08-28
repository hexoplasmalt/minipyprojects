from fractions import Fraction

def convert(type,inp):
    if type == "p":
        decimal = float(inp[:-1]) / 100
        print(f"{inp} = {decimal} = {Fraction(decimal).limit_denominator().as_integer_ratio()}")
    if type == "f":
        n,d = inp.split("/")
        decimal = float(n)/float(d)
        print(f"{inp} = {decimal*100:g}% = {decimal}")
    if type == "d":
        print(f"{inp} = {Fraction(float(inp)).limit_denominator().as_integer_ratio()} = {float(inp)*100:g}")

while True:
    match input("Enter fraction (N/D), decimal or percentage (%) [q for quit]: "):
        case s if s.endswith("%") : convert("p",inp)
        case s if "/" in s : convert("f",inp)
        case s if "." in s : convert("d",inp)
        case s if s.lower() == "q" : break
        case _ : print("Invalid input.")