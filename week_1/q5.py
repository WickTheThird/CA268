
class Test:

    def __init__(self, subject, cor_answ=[], per=''):
       
        self.subject = subject
        self.cor_answ = cor_answ
        self.per = per
    
class Student:

    def __init__(self, name):
        self.name = name
    
    def take_test(self, other, stud_answ=[]):

        cor_st_answ = 0

        for i, x in enumerate(stud_answ):

            if x == other.cor_answ[i]:
                cor_st_answ += 1
        
        final_grade = (cor_st_answ * 100) / len(other.cor_answ)
        passing_graade = other.per.split("%")
        passing_grade = int(passing_graade[0])
        
        if stud_answ == other.cor_answ or final_grade >= passing_grade:

            print(f'{self.name} passed the Chemistry test with the score {final_grade}%')

        else:

            print(f'{self.name} failed the Maths test!')
