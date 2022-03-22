print('Hello from VS CODE!!')


def hello():
    print('hello')


def pack(*args):
    print([*args])


pack('but', 'nicely')

def eat_luch(lst=[]):
    for food in lst:
        if lst.index(food) == 0:
            print(f"I eat {food}")
        else: 
            print(f"I also eat {food}")

eat_luch(['peanut butter', 'grpaes', 'ponchos'])