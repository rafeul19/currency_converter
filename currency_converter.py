
#Class Declaration
class CurrencyConverter:
    exchange_rates = {
        "USD" : 1.0,
        "BDT" : 121.75,
        "EUR" : 0.88,
        "GBP" : 0.75
    }
    #class attribute #base value dollar
    #Class Arrtibute (( OK ))
    
    #Object Initialization and self 
    def __init__(self, amount, from_currency, to_currency):
        
        self.amount = amount
        self.from_currency = from_currency
        self.to_currency = to_currency
        #Self of values added 
        
    #Instance method
    
    def convert(self):
        if self.from_currency not in CurrencyConverter.exchange_rates or \
        self.to_currency not in CurrencyConverter.exchange_rates:
            return "You have entered an invalid currency input that not in our system"
        
        
        #Convertion
        
        base_amount = self.amount / CurrencyConverter.exchange_rates[self.from_currency]
        converter_amount = base_amount * CurrencyConverter.exchange_rates[self.to_currency] 
        
        return round(converter_amount, 2) #Returning amount up to 2 decimal places
    
    
    #Update Rate value
    @classmethod
    def update_rate(cls, currency, new_rate):
         cls.exchange_rates[currency] = new_rate
         
    @staticmethod #Helper function
    def is_valid_currency(code):
        return code.upper() in CurrencyConverter.exchange_rates
    
    class Logger : 
        
        def Log(self, user, converter):
            result = converter.convert()
            print(f"record: {user} converted {converter.amount} {converter.from_currency} -> {result} {converter.to_currency}")
            
            
            
if __name__ == "__main__": 
    amount = float(input("Enter the amount: "))
    from_curr = input ("Enter the currency : ")
    to_curr = input("Enter Your Desired Currency In Which You Want TO Convert: ")
    user = input("Enter Your Name: ")
        
    converter = CurrencyConverter(amount, from_curr, to_curr)
        
    if not CurrencyConverter.is_valid_currency(from_curr) or not CurrencyConverter.is_valid_currency(to_curr):
        print("Invalid currency code. Please enter a valid currency code.")
    else:
        Logger_object = CurrencyConverter.Logger()
        Logger_object.Log(user, converter)
    