import csv

book_of_john = open("book of John text.txt", "r")
book_of_john_file = csv.reader(book_of_john, delimiter = " ")



john_dict ={}

#The variable word is still in a list. I think you need
#   to convert the list to a dictionary. Though you
#   may just need to put the list in the dictionary?

#Search line by line here
for word in book_of_john_file:
    if word in john_dict:
        john_dict[word] += 1
    else:
        john_dict[word] = 1

        
#Can use the f string method

print(f"Father: {john_dict['Father']}")
    #print(type(word))



book_of_john.close()
#Do I want to add all the words to a dictionary,
#   then count the number of times it appears
#   in the dictionary?


#The key is the word, the value is the count

"""
import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")

# to skip a line if the file contains a header record
next(customer_file)

for record in customer_file:
    print(record)

    print("first name:", record[1])
    print("last name:", record[2])
    print("City:", record[3])
    print("Country:", record[4])
    print("Phone:", record[5])

    input()
"""