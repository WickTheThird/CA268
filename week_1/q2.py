
def move_vow(line):
    
    vow = 'aeiouAEIOU'

    final_vow = ''
    final_cos = ''

    for x in line:

        if x in vow:

            final_vow += x

        else:

            final_cos += x

    final = final_vow + final_cos
    
    return final
