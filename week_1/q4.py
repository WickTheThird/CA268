
class Memories:

    def __init__(self, name, age=0, salary=0):

       self.name = name
       self.age = age
       self.salary = salary

    def remember(self, info):

        match info:

            case "name":
                return self.name
            case "salary":
                return self.salary
            case "age":
                return self.age
        
        return False
