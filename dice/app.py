import random

def main():
    x=int(random.uniform(1,6))
    y=int(random.uniform(1,6))

    print("Die 1: "+str(x))
    print("Die 2: "+str(y))

    total=x+y
    
    print("Total value: "+str(total))

if __name__ == "__main__":
    print("Rolling the dice...")
    main()