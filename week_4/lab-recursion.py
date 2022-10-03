
#Q1

def sunmming(num_list, ind):

    if (ind + 1) == len(num_list):

        return num_list[ind]

    return num_list[ind] + sunmming(num_list, ind + 1)

#Q2

def rev_int(nr):
    
    nr = str(nr)

    if len(nr) == 0:
        return nr

    return nr[-1] + rev_int(nr[:-1])

#Q3

def rev_str(the_str):

    if len(the_str) == 0:

        return the_str
    
    return the_str[-1] + rev_str(the_str[:-1])

#Q4

def rev_li(the_li):

    if len(the_li) == 1:

        return [the_li[0]]

    return [the_li[-1]] + rev_li(the_li[:-1])

#Q5

def multiply(nr, times):
    
    if times == 1:

        return nr

    return nr + multiply(nr, times - 1)

#Q6

def is_heteromecic(the_nr, const=0):
    
    if the_nr < 0:
        return False

    if the_nr * (the_nr + 1) == (the_nr + const):
        return True

    elif the_nr == 0:
        return False
    
    return is_heteromecic(the_nr - 1, const + 1)    

#Q7

def which_len(the_stry):

    if len(the_stry) == 0:
        return 0

    return 1 + which_len(the_stry[:-1])
