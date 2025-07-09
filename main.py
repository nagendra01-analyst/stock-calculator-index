class CompanyData:
    def get_company_stock(self):
        # Format: [company_name, number_of_stocks, stock_code]
        return [
            ['company1', 20, 'abc'],
            ['company1', 25, 'xyz'],
            ['company2', 38, 'aaa'],
            ['company2', 10, 'xyz'],
            ['company3', 15, 'abc']
        ]

class PriceData:
    def get_stock_prices(self):
        # Format: [stock_code, price]
        return [['abc', 10], ['xyz', 20], ['aaa', 5]]

class StockCalculator:
    def calculate_total_stock_price(self):
        company_obj = CompanyData()
        price_obj = PriceData()

        company_stocks = company_obj.get_company_stock()
        stock_prices = price_obj.get_stock_prices()

        # Convert stock prices list to a dictionary for quick lookup
        price_map = {code: price for code, price in stock_prices}
        result = {}

        for company, qty, code in company_stocks:
            price = price_map.get(code, 0)
            total = qty * price

            if company in result:
                result[company] += total
            else:
                result[company] = total

        # Output the total stock price for each company
        for company, total_price in result.items():
            print(f"{company} : ${total_price}")

# Run the calculator
if __name__ == "__main__":  
    calc = StockCalculator()
    calc.calculate_total_stock_price()
