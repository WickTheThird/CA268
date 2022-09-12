
guests = {
    'Randy': 'Germany',
    'Karla': 'France',
    'Wendy': 'Japan',
    'Norman': 'England',
    'Sam': 'Argentina'
}


def greetings(name):

    if name in guests:

        return f"Hi! I'm {name} and I'm from {guests[name]}."
    else:

        return f"Hi, I'm {name}."
