# Stock Portfolio Tracker

# Stock prices (sample prices for practice)
stock_prices = {
    "TCS": 3500,
    "Infosys": 1800,
    "Wipro": 550,
    "Reliance": 2900,
    "HDFC": 1700
}

print("Welcome to Stock Portfolio Tracker!")
print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(stock, ":", price)

# Create an empty portfolio
portfolio = {}
total_investment = 0

# Allow the user to enter multiple stocks
while True:
    stock = input(
        "\nEnter stock name (or type 'exit' to finish): "
    ).strip()

    # Exit the loop
    if stock.lower() == "exit":
        break

    # Match stock names without case sensitivity
    stock_lookup = {name.lower(): name for name in stock_prices}
    stock = stock_lookup.get(stock.lower())

    if stock is None:
        print("Sorry, stock not available. Please try again.")
        continue

    print("Stock found!")
    print("Price per share: ₹", stock_prices[stock])

    # Validate quantity input
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if quantity <= 0:
        print("Please enter a quantity greater than zero.")
        continue

    # Calculate cost
    total_cost = stock_prices[stock] * quantity

    # Store stock and quantity
    portfolio[stock] = portfolio.get(stock, 0) + quantity

    # Update total investment
    total_investment += total_cost

    print(
        "Cost for", quantity, "shares of", stock,
        "is: ₹", total_cost
    )

# Display the final portfolio
print("\n========== YOUR PORTFOLIO ==========")

if portfolio:
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        cost = price * quantity

        print(
            stock,
            "| Quantity:", quantity,
            "| Price: ₹", price,
            "| Total: ₹", cost
        )

    print("------------------------------------")
    print("Total investment: ₹", total_investment)

else:
    print("Your portfolio is empty.")

print("Thank you for using Stock Portfolio Tracker!")

# Save portfolio to a text file
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        cost = price * quantity

        file.write(
            f"{stock} - Quantity: {quantity}, "
            f"Price: Rs.{price}, Total: Rs.{cost}\n"
        )

    file.write(f"\nTotal Investment: Rs.{total_investment}\n")

print("Your portfolio has been saved to portfolio.txt")