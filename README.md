# Stock Portfolio Tracker Using Python

## 1. Project Overview

The Stock Portfolio Tracker is a simple Python-based application that helps users calculate the total investment value of their stock portfolio.

Users can enter stock names and quantities. The application uses predefined stock prices stored in a Python dictionary to calculate individual stock investments and the overall portfolio value.

The project also provides an option to save portfolio details in TXT and CSV file formats.

## 2. Project Objectives

- To develop a simple stock portfolio tracking application using Python.
- To accept stock names and quantities from users.
- To store predefined stock prices using dictionaries.
- To calculate individual and total investment values.
- To save portfolio reports using file handling.

## 3. Features

- User input for stock names.
- User input for stock quantities.
- Predefined stock prices using a dictionary.
- Automatic investment calculation.
- Portfolio summary display.
- Save reports in TXT format.
- Save reports in CSV format.
- Input validation and error handling.

## 4. Technologies Used

- **Programming Language:** Python
- **IDE:** Visual Studio Code
- **Data Structure:** Dictionary
- **File Handling:** TXT and CSV
- **Python Modules:** csv, datetime

## 5. Stock Price Dictionary

The application uses predefined stock prices.

Example:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 175,
    "NVDA": 140
}
```

These are sample hardcoded prices and are not live market prices.

## 6. Calculation Formula

Individual Stock Investment:

Stock Price × Quantity

Total Portfolio Investment:

Sum of all individual stock investments.

## 7. Project Structure

```text
Stock_Portfolio_Tracker/
│
├── main.py
├── portfolio.txt
├── portfolio.csv
└── README.md
```

The TXT and CSV files are generated when the user saves the portfolio report.

## 8. How to Run the Project

**Step 1:** Install Python 3.

**Step 2:** Open the project folder in Visual Studio Code.

**Step 3:** Open the terminal.

**Step 4:** Run the following command:

```bash
python main.py
```

**Step 5:** Enter stock names and quantities.

**Step 6:** View the total investment value.

**Step 7:** Choose an option to save the portfolio report.

## 9. Example

Sample Input:

```text
AAPL
10
TSLA
5
MSFT
2
DONE
```

Expected Calculation:

- AAPL = 10 × 180 = $1800
- TSLA = 5 × 250 = $1250
- MSFT = 2 × 400 = $800

Total Investment = $3850

## 10. Expected Output

The application displays a portfolio summary containing:

- Stock name
- Quantity
- Stock price
- Individual investment
- Total investment value

Users can also save the results in TXT or CSV format.

## 11. Concepts Learned

- Python dictionaries
- Variables and data types
- User input and output
- Conditional statements
- Loops
- Functions
- Arithmetic operations
- File handling
- Exception handling

## 12. Future Improvements

- Integrate real-time stock market prices through a reliable market data API.
- Add a graphical user interface.
- Store portfolio information in a database.
- Display portfolio performance using charts.

## 13. Conclusion

The Stock Portfolio Tracker demonstrates how Python can be used to develop a simple financial tracking application. It provides practical experience with dictionaries, functions, arithmetic operations, user input, and file handling.

---

**Project Name:** Stock Portfolio Tracker

**Language:** Python

**Project Type:** Internship Project
