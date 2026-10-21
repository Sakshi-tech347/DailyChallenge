
def Addition(no1 ,no2):
    Ans = 0
    Ans = no1+ no2

    return Ans

def Substraction(no1 ,no2):
    Ans = 0
    Ans = no1 - no2

    return Ans

def main():
    print("Enter First number")
    value1 = int(input())

    print("Enter Second number")
    value2 = int(input())

    Ret = Addition(value1,value2)
    print("Additin of two number is ",Ret)

    Ret = Substraction(value1,value2)
    print("Substraction of two number is ",Ret)

if __name__ =="__main__":
    main()
