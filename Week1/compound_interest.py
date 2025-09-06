P = float(input("Enter initial deposit: "))
r = float(input("Enter interest rate in decimals: "))
n = int(input("Enter number of times interest is compounded a year: "))
t = float(input("Enter number of years the initial deposit is invested for: "))

future_value = P * (1 + r/n)**(n*t)

print(f'The future value of initial amount {P} with interest of {r}, compounded {n} times a year for {t} years is {future_value}')