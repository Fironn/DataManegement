import random

def main(name):
    x=int(random.uniform(1,6))
    y=int(random.uniform(1,6))
    z=int(random.uniform(1,6))

    print("Die 1: "+str(x))
    print("Die 2: "+str(y))
    print("Die 3: "+str(z))

    total=x+y+z
    print("Total value: "+str(total))

    if total > 7:
        print(name+" won!")
    else:
        print(name+" lost!")

    print("You get "+fizzBuzz(total))

def fizzBuzz(num):
    if num%3==0 and num%5==0:
        return "FizzBuzz"
    elif num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    else:
        return str(num)

def askName():
    name=input("What is your name?\n> ")
    print(name)
    print("Hallo, "+name+"!")

    return name


if __name__ == "__main__":
    name=askName()
    print("Rolling the dice...")
    main(name)