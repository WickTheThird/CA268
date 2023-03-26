
def  filter_star(the_dict, nr_stars):

    new_dict = {}
    
    for x in the_dict:

        if len(the_dict[x]) == nr_stars:

            new_dict[x] = '*' * nr_stars
    
    if len(new_dict) == 0:
        return 'No result found!'
    
    else:
        return new_dict
