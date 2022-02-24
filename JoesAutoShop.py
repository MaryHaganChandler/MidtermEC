from tkinter import Y


class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone



class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, y):
        self.__year = y

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year



class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__pcharge = pcharge
        self.__lcharge = lcharge
    
    def set_parts_charges(self, pcharge):
        self.__pcharge = pcharge

    def set_labor_charges(self, lcharge):
        self.__lcharge = lcharge

    def get_part_charges(self, pcharge):
        return self.__pcharge

    def get_labor_charges(self, lcharge):
        return self.__lcharge

    def get_sales_tax(self):
        return 0.07

    def get_total_charges(self, pcharge, lcharge):
        total_charges = (pcharge + lcharge)*0.07
        return total_charges


#Questions:
#   1) What do I put for get_sales_tax?
#   2) Do I do the calculation in get_total_charges? Shouldn't I have
#      a separate method? How do I reference the sales tax?