import math as m
def generatingNewList(lst1, lst2):
    if len(lst1) != len(lst2):
        return []
    newList = []
    for z in range(len(lst1)):
        x=lst1[z]
        y=lst2[z]
        if x % 2 == 0 and y % 2 == 0:
            newList.append(x+y)
        elif x % 2 == 1 and y % 2 == 1:
            newList.append(x*y)
        else:
            newList.append(x-y)
    return newList

    

def generateListPrime(lst):
    def checkPrime(val):
        for x in range(2, int(m.sqrt(val))+1):
            if val%x==0:
                return False
        return True
    newList = []
    for y in lst:
        if checkPrime(y)and y != 0 and y != 1:
            newList.append(y)
    return newList

def main():
    print("Making the calls of the implemented methods")
    print(generatingNewList([2,3,40,7],[10,5,15,2]))
    print(generateListPrime([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    

if __name__ == "__main__":
    main()
