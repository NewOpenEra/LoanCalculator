import math

MONTHS_IN_YEAR = 12


def num_of_payments():
    print("Enter the loan principal: ")
    principal = int(input())
    print("Enter the monthly payment: ")
    payment = int(input())
    print("Enter the loan interest: ")
    interest = float(input())

    # Calculate the nominal interest rate
    i = interest / (MONTHS_IN_YEAR * 100)

    # Calculate the number of months until the loan is repaid
    x = payment / (payment - i * principal)
    total_monthly_payments = math.ceil(math.log(x, 1 + i))

    # Output the answer to the user
    # Method to handle singular or plural response
    def pluralize(n, singular, plural):
        return f"{n} {singular if n == 1 else plural}"

    if total_monthly_payments < MONTHS_IN_YEAR:
        print(f"It will take {pluralize(total_monthly_payments, 'month', 'months')} to repay the loan.")
    elif total_monthly_payments == MONTHS_IN_YEAR:
        print("It will take 1 year to repay this loan!")
    else:
        years = total_monthly_payments // MONTHS_IN_YEAR
        months = math.ceil(total_monthly_payments % MONTHS_IN_YEAR)

        if months != 0:
            print(
                f"It will take {pluralize(years, 'year', 'years')} and {pluralize(months, 'month', 'months')} to repay this loan!")
        else:
            print(f"It will take {pluralize(years, 'year', 'years')} to repay this loan!")


def monthly_payment_amount():
    print("Enter the loan principal: ")
    principal = int(input())
    print("Enter the number of periods: ")
    periods = int(input())
    print("Enter the loan interest: ")
    interest = float(input())

    # Calculate the nominal interest rate
    i = interest / (MONTHS_IN_YEAR * 100)

    # Calculate the ordinary annuity rounded up to nearest unit
    annuity = math.ceil((principal * ((i * pow(1+i, periods)) / (pow(1+i, periods) - 1))))

    # Output answer to the user
    print(f"Your monthly payment = {annuity}!")


def calculate_principal():
    print("Enter the annuity payment: ")
    annuity = float(input())
    print("Enter the number of periods: ")
    periods = int(input())
    print("Enter the loan interest: ")
    interest = float(input())

    # Calculate the nominal interest rate
    i = interest / (MONTHS_IN_YEAR * 100)

    # Calculate the load principal rounded up to the nearest unit
    principal = round(annuity / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))

    # Output answer to the user
    print(f"Your loan principal = {principal}!")


print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: ''')

choice = input()

if choice == "n":
    num_of_payments()
elif choice == "a":
    monthly_payment_amount()
elif choice == "p":
    calculate_principal()
