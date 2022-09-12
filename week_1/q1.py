
def q1_sum(list_el):

    total = 0

    for el in list_el:

        try:
            if el % 2 == 0:
                total += el

        except TypeError:

            for x in el:
                if x % 2 == 0:
                    total += x

    return total
