from functools import reduce
def main():

    data = [10,20,39,46,33,21,34]

    print("Actual data ", data)

    Fdata = (list(filter(lambda No : No % 2==0 , data)))
    print("Filter data is ",Fdata)

    Mdata = (list(map(lambda N : N + 1, Fdata)))
    print("Maped data is :",Mdata)

    RData = (reduce(lambda A,B : A+B , Mdata))
    print("Reduced data is ", RData)


if __name__ == "__main__":
    main()