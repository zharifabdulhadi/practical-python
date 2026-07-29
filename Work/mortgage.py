# mortgage.py
#
# Exercise 1.7

### Exercise 1.8: Extra payments

# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
# Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.
# When you run the new program, it should report a total payment of `929,965.62` over 342 months.

### Exercise 1.9: Making an Extra Payment Calculator
# Modify the program so that extra payment information can be more generally handled.
# Make it so that the user can set these variables:

# ```python
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000
# ```

# Make the program look at these variables and calculate the total paid appropriately.

# How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first
# five years have already been paid?

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    month += 1

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    print(month, round(total_paid, 2), round(principal, 2))
print('Total paid', round(total_paid,2))
print('Months', round(month))