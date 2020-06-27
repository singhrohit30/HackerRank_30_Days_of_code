# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
# and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

# Complete the solve function below.


def solve(meal_cost, tip_percent, tax_percent):
    tip = (tip_percent / 100) * meal_cost
    tax = (tax_percent / 100) * meal_cost
    total_bill = round(meal_cost + tip + tax)
    return total_bill


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    result = solve(meal_cost, tip_percent, tax_percent)
    print(result)
