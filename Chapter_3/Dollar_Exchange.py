# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


x_rate = 0.65  # Exchange rate to English Pounds
total_dollars = 200  # Total American Dollars
fee = 2  # In American Dollars
total_pounds = (total_dollars - fee) * x_rate  # Total English Pounds after exchange
total_dollars = (total_pounds - 100) / x_rate - fee  # Left over American Dollars
print(total_dollars)
