def read_unit():
    n = int(input())
    return n


def calculate(n):
    if n <= 50:
        amt = n * 0.50

    elif (n > 50) and (n <= 150):
        amt = 25 + (n - 50) * 0.75

    elif (n > 150) and (n <= 250):
        amt = 100 + (n - 150) * 1.20
    else:
        amt = 220 + (n - 250) * 1.50
    sur_charge = amt * 0.20

    net_amt = sur_charge + amt
    return net_amt


def display_result(total):
    print("Total amount=", total)
    return


unit = read_unit()
while unit > 0:
    total = calculate(unit)
    display_result(total)
    unit = read_unit()
