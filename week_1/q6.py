
def histogram(line, type):

    final = [''] * len(line)

    for i, x in enumerate(line):

        final[i] = (type * x)

        print(final[i])


histogram([6, 2, 15 , 3, 20 , 5], '=')
