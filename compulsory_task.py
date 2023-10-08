
#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost 
        self.quantity = quantity


    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity
        
    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f'Country is {self.country}, The code is {self.code}, The product is {self.product}, Cost is {self.cost}, The quantity is {self.quantity}'
        
# =========Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open ("inventory.txt", "r") as file:
            for lines in file:
                temp = lines.strip()
                temp = temp.split(",")

                shoe_list.append(Shoe(temp[0]))
    
    except:
        print("error reading file.")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("Please enter your country: ")
    code = input("Please enter your code: ")
    product = input("Please enter the product: ")
    cost = input("Enter the cost: ")
    quantity = input("Enter quantity please: ")
    shoe_list.append(Shoe(country, code, product, cost, quantity))

    with open ("inventory.txt", "r") as f:
        f.write(f"{country}, {code}, {product}, {cost}, {quantity}\n")

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for shoe in shoe_list:
        print(shoe)
        
def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    minimum = sorted(shoe_list, key = lambda x: x.quantity) [:1]
    for lowest_shoe in minimum:
        print(lowest_shoe)
        print("Would you like to add this quantity of shoe?")
        answer = input("Yes/No: ")
        if answer == "Yes":
            add_quantity = int(input("Enter the new quantity here: "))
            lowest_shoe.quantity = add_quantity

        with open ("inventory.txt", "r") as f:
            lines = f.readlines()
        with open ("inventory.txt", "w") as f:
            for line in lines:
                if line.strip().split(",")[1] != lowest_shoe.code:
                    f.write(line)
                else:
                    f.write(f"{lowest_shoe.country}. {lowest_shoe.code}, {lowest_shoe.product}, {lowest_shoe.cost}. {lowest_shoe.quantity}")

def seach_shoe(code):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
        
        return None

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"The total value is {value}")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    highest_product = sorted(shoe_list, key = lambda x: x.quantity, rewind = True)
    for product in highest_product:
        print(product)


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def main():
    read_shoes_data()

while True:
    print('''\n Menu:
        1. Capture the shoe data.
        2. view all the shoes.
        3. Restock the show that has the lowest quantity.
        4. Search a shoe using the code.
        5. Calue the value per item.
        6. Determine the product with the highest quantity.
        7. Exit program.    ''')
    
    desicion = input("Enter your desicion here: ")

    if desicion == "1":
        capture_shoes()

    elif desicion == "2":
        view_all()

    elif desicion == "3":
        re_stock()

    elif desicion == "4":
        code = input("Enter the code for shoe: ")
        product = seach_shoe(code)
        if product:
            print(product)
        
        else:
            print("Product is not found.")

    elif desicion == "5":
        value_per_item()

    elif desicion == "6":
        highest_qty()

    elif desicion == "7":
        break

    else: 
        print("Invalid choice.")

#Now i will just write code to allow for the menu function to run.
main()
