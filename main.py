import math
import argparse


MONTHS_IN_YEAR = 12

parser = argparse.ArgumentParser(description="Loan Calculator")

parser.add_argument("--type", choices=["annuity", "diff"], help="You need to choose the type of payment")
parser.add_argument("--interest", type=float, help="The interest rate of the loan")
parser.add_argument("--principal", type=int, help="The loan principal amount")
parser.add_argument("--periods", type=int, help="The total number of repayments to be made")
parser.add_argument("--payment", type=int, help="The payment amount each period")

group = parser.add_mutually_exclusive_group()
group.add_argument("--annuity", action="store_true", help="Calculate annuity payment")
group.add_argument("--diff", action="store_true", help="Calculate differentiated payment")

args = parser.parse_args()
calc_type = args.type
principal = args.principal
interest = args.interest
payment = args.payment
periods = args.periods


def num_of_payments():

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

    print(f"Overpayment = {total_monthly_payments * payment - principal}")


def monthly_annuity_payment():

    # Calculate the nominal interest rate
    i = interest / (MONTHS_IN_YEAR * 100)

    # Calculate the ordinary annuity rounded up to nearest unit
    annuity = math.ceil((principal * ((i * pow(1+i, periods)) / (pow(1+i, periods) - 1))))

    # Output answer to the user
    print(f"Your monthly payment = {annuity}!")
    print(f"Overpayment = {annuity * periods - principal}")


def monthly_differentiated_payment():

    # Calculate the nominal interest rate
    i = interest / (MONTHS_IN_YEAR * 100)

    dm_sum = 0.0

    for m in range(1,periods+1):
        dm = math.ceil(principal / periods + i * (principal - ((principal * (m - 1)) / periods)))
        dm_sum += dm
        print(f"Month {m}: payment is {dm}")

    print(f"\nOverpayment = {dm_sum - principal}")



def calculate_principal():

    # Calculate the nominal interest rate
    i = interest / (MONTHS_IN_YEAR * 100)

    # Calculate the load principal rounded up to the nearest unit
    principal = math.floor(payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))

    # Output answer to the user
    print(f"Your loan principal = {principal}!")

    print(f"Overpayment = {payment * periods - principal}")


# Sanity Checks: Print "Incorrect Parameters" warning if:
# no type or invalid type is chosen
if not calc_type or (calc_type != "annuity" and calc_type != "diff"):
    print("Incorrect Parameters")
# differentiated payment type is chosen, but a payment value is entered
elif args.type == "diff" and payment:
    print("Incorrect Parameters")
# an Interest value is not entered
elif not interest:
    print("Incorrect Parameters")
# insufficient parameters are entered
elif sum(arg is not None for arg in [args.type, args.principal, args.payment, args.periods, args.interest]) < 4:
    print("Incorrect parameters")
else:
    # Call appropriate functions
    if args.type == "annuity":
        if not principal:
            calculate_principal()
        elif not periods:
            num_of_payments()
        else:  # not payment:
            monthly_annuity_payment()
    else:  # if args.type == "diff"
        monthly_differentiated_payment()