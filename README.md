# Currency Converter Application
# This Python script implements a currency conversion tool with exchange rate management and logging capabilities

## Overview
This code provides a currency conversion system that:
1. Converts between supported currencies using predefined exchange rates
2. Allows updating exchange rates dynamically
3. Validates currency codes
4. Logs conversion requests with user information

Supported currencies: USD, BDT, EUR, GBP

## Key Components
1. **Class Attributes**:
   - `exchange_rates`: Dictionary storing current exchange rates (base currency is USD)

2. **Instance Methods**:
   - `convert()`: Performs currency conversion calculation
   - `__init__()`: Initializes conversion parameters

3. **Class Methods**:
   - `update_rate()`: Updates exchange rate for a specific currency

4. **Static Methods**:
   - `is_valid_currency()`: Checks if a currency code is valid

5. **Nested Logger Class**:
   - `Log()`: Records conversion details with user information

## How to Run
```bash
# Run the currency converter application
python currency_converter.py


