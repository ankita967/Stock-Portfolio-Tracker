
import csv
from datetime import datetime

# Step 1: Define stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 175,
    "NVDA": 140
}

# Step 2: Store portfolio information
portfolio = {}

# Step 3: Display available stocks
def display_stocks():
    print("\n========== AVAILABLE STOCKS ==========")

    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

# Step 4: Add stocks to portfolio
def add_stock():
    display_stocks()

    while True:
        stock = input("\nEnter stock name (or DONE to finish): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found! Please enter a valid stock.")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid whole number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print(f"{quantity} shares of {stock} added successfully!")

# Step 5: Calculate investment
def calculate_investment():
    total_investment = 0

    print("\n========== PORTFOLIO SUMMARY ==========")
    print(f"{'Stock':<12}{'Quantity':<12}{'Price':<12}{'Total':<12}")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        print(
            f"{stock:<12}{quantity:<12}"
            f"${price:<11.2f}${investment:<11.2f}"
        )

    print("---------------------------------------")
    print(f"Total Investment: ${total_investment:.2f}")

    return total_investment

# Step 6: Save portfolio in TXT file
def save_txt(total):
    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("======================\n\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Investment: ${investment}\n"
            )

        file.write(f"\nTotal Investment: ${total:.2f}\n")
        file.write(f"Generated: {datetime.now()}\n")

    print("TXT report saved successfully!")

# Step 7: Save portfolio in CSV file
def save_csv(total):
    with open("portfolio.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Stock Name",
            "Quantity",
            "Stock Price",
            "Total Investment"
        ])

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            writer.writerow([
                stock,
                quantity,
                price,
                investment
            ])

        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])

    print("CSV report saved successfully!")

# Step 8: Main program
def main():

    print("===================================")
    print("      STOCK PORTFOLIO TRACKER")
    print("===================================")

    add_stock()

    if not portfolio:
        print("\nNo stocks were added to your portfolio.")
        return

    total = calculate_investment()

    while True:
        print("\n========== SAVE OPTIONS ==========")
        print("1. Save as TXT")
        print("2. Save as CSV")
        print("3. Save both")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            save_txt(total)

        elif choice == "2":
            save_csv(total)

        elif choice == "3":
            save_txt(total)
            save_csv(total)

        elif choice == "4":
            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()

