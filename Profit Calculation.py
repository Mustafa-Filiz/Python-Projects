sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  

# the profit will be : 13130

profit = sales["sell_value"] - sales["cost_value"]  # profit from each product
total_profit = sales["inventory"] * profit
print(round(total_profit))