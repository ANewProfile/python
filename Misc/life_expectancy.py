years = float(input("What is your age(yrs)? "))


def returns(yrs):
    val = 90 - yrs
    wk = val * 52
    month = val * 12
    return [val, wk, month]


value = returns(years)

print(
    f"You have {value[0]} years, {value[1]} weeks, and {value[2]} months left(life expectancy 90 yrs).")
