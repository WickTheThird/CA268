#Q1

class Stuff:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def get_email(self):
        email = self.fname + '.' + self.lname  + '.dcu.ie'
        return email

#Q2

class Stuff2:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return "{} is {} years old".format(self.name, str(self.age))

    def get_height(self):
        return "{} is {} cm tall".format(self.name, str(self.height))

    def get_weight(self):
        return "{} is {} kg".format(self.name, str(self.weight))


#Q3

class Class4:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

def sort_class4(obj_list, atribute):

    sorting_list = []
    for x in obj_list:

        match atribute:
            case 'fname':
                sorting_list.append(x.fname)
            case 'lname':
                sorting_list.append(x.lname)
            case 'age':
                sorting_list.append(x.age)

    sorting_list.sort()

    return sorting_list

#Q4

class Smoothie:

    def __init__(self, ingr_list):
        
        self.ingredients = {
            'Banana': 0.50,
            'Strawberries': 1.50,
            'Mango': 2.50,
            'Blueberries': 1.00,
            'Raspberries': 1.00,
            'Apple': 1.75,
            'Pineapple': 3.50
        }

        self.ingr_list = ingr_list

    def get_cost(self):

        total = 0
        for x in self.ingr_list:
            if x in self.ingredients:
                total += self.ingredients[x]

        return '€{:.2f}'.format(total)
    
    def get_price(self):

        costs = self.get_cost().split("€")
        total = float(costs[1]) + 2.5

        return '€{:.2f}'.format(total)

    def get_name(self):

        if len(self.ingr_list) == 1:
            return self.ingr_list[0] + ' Smoothie'

        else:
            all_ingr = " ".join(self.ingr_list) + " Fusion"
            return all_ingr

#Q5

class Pizza(object):

    total_li = []

    def __init__(self, ingredients=[]):

        Pizza.total_li.append(ingredients)
        self.order_number = len(Pizza.total_li)

        if len(Pizza.total_li) > 0:
            self.ingredients = Pizza.total_li[self.order_number - 1]
    
    def diavola():
        return Pizza(['Mozzarella', 'Spicy sausage', 'Pomodorino tomatoes'])
    
    def serrano():
        return Pizza(['Black olives', 'Red onion', 'Meatballs'])

    def margherita():
        return Pizza(['Red tomatoes', 'White mozzarella', 'Green basil'])

#Q6

class Employee:

    def __init__(self, name, **kwargs):

        name = name.split(" ")
        self.firstname = name[0]
        self.lastname = name[-1]       

        for key, value in kwargs.items():
            self.__dict__[key] = value


