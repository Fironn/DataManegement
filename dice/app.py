import random

def main():
    x=int(random.uniform(1,6))
    y=int(random.uniform(1,6))

    print("Die 1: "+str(x))
    print("Die 2: "+str(y))

    total=x+y

    print("Total value: "+str(total))


def askName():
    name=input("What is your name?\n")
    print(name)
    print("Hallo, "+name+"!")


if __name__ == "__main__":
    askName()
    print("Rolling the dice...")
    main()