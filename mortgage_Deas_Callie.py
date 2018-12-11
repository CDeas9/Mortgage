def main():
    cost = float(input('How much does the house cost? '))
    down = float(input('What percentage are you putting down? '))
    percent = down/100
    money_down = float(cost*percent)
    total = cost-money_down
    print('You are putting down ' + str(money_down) + ' leaving ' + str(total) + ' for the mortgage')
    years = float(input("How many years does the mortgage last? "))
    interest = float(input("What is your interest rate? "))
    perc_intr = interest/100
    payments = int(years*12)
    monthly = calc_monthly(total, perc_intr, payments)
    print('You will make ' + str(payments) + ' payments of ' + str(monthly))


def calc_monthly(p, r, m):
    top = p*(r/12)
    bottom = (1-(1+r/12)**-m)
    monthly = top/bottom
    return monthly


main()
