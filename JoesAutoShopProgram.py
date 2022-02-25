#You also need a program file that generates a service quote
import JoesAutoShopClass as jasc

def main():
    #Define variables for customer.
    name = "Mary Chandler"
    address = "1234 Main Street"
    phone = "(555)555-5555"

    #Define variables for car.
    make = "Toyota"
    model = "Corolla"
    year = 2019

    #Define variables for the charges.
    parts_charge = 85
    labor_charge = 105

    #Create customer, car, and service_quote instances.
    customer = jasc.Customer(name, address, phone)
    car = jasc.Car(make, model, year)
    service_quote = jasc.ServiceQuote(parts_charge, labor_charge)

    #Print out the service quote.
    print("\t   Service Quote")
    print("Customer Name:\t  ", customer.get_name())
    print("Customer Address: ", customer.get_address())
    print("Customer Phone:\t  ", customer.get_phone())
    print("Car Description:  ",car.get_year(),car.get_make(),car.get_model())
    print("Labor Charges:\t  ", service_quote.get_labor_charges())
    print("Parts Charges:\t  ", service_quote.get_part_charges())
    print("Sales Tax:\t  ", service_quote.calculate_sales_tax())
    print("Total Charges:\t  ", service_quote.calculate_total_charges())

#Run the main() method.
main()