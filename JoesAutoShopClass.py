#Define a sales tax constant.
SALES_TAX = 0.0825

#Create a Customer class.
class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    #Set methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    #Get methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


#Create a Car class.
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    #Set methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, y):
        self.__year = y

    #Get methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year


#Create a ServiceQuote class.
class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__pcharge = pcharge
        self.__lcharge = lcharge
    
    #Set methods
    def set_parts_charges(self, pcharge):
        self.__pcharge = pcharge

    def set_labor_charges(self, lcharge):
        self.__lcharge = lcharge

    #Get methods
    def get_part_charges(self):
        return self.__pcharge

    def get_labor_charges(self):
        return self.__lcharge

    def calculate_sales_tax(self):
        sales_tax = (self.__pcharge + self.__lcharge) * SALES_TAX
        return sales_tax

    def calculate_total_charges(self):
        total_charges = (self.__pcharge + self.__lcharge) * (1 + SALES_TAX)
        return total_charges