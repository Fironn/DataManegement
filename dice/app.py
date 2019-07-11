import random

def main(name):
    x=int(random.uniform(1,6))
    y=int(random.uniform(1,6))

    print("Die 1: "+str(x))
    print("Die 2: "+str(y))

    total=x+y

    print("Total value: "+str(total))

    if total > 7:
        print(name+" won!")
    else:
        print(name+" lost!")


def askName():
    name=input("What is your name?\n> ")
    print(name)
    print("Hallo, "+name+"!")

    return name


if __name__ == "__main__":
    name=askName()
    print("Rolling the dice...")
    main(name)