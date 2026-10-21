


checkEven = lambda no1 : no1%2==0

def main():
    print("enter number ")
    value = int(input())

    Ret =checkEven(value)

    if(Ret == True):
        print("Even")

    else:
        print("Odd")




if __name__ == "__main__":
    main()