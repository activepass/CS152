def generatingNewList(lst1, lst2):
    '''
    Generates a new list based on the following rules:
        - compare elements in the same index for both lists
        
        - if the elements in the same index on lst1
        and lst2 are both even, add those elements and
        store the result in the same index in the new list
                    
        - if the elements in the same index on lst1
        and lst2 are both odd, multiply those elements and
        store the result in the same index in the new list
        
        - if one of the element in the same index is even and
        the other element in the same index is odd, subtract
        the element in lst2 from lst1
        
        For example:
        lst1   = [ 2,  3, 40, 7]
        lst2   = [10,  5, 15, 2]
        newLst = [12, 15, 25, 5]
        
    This function will return the new list when both parameters
    (lst1 and lst2) have the exact same length.
    If the parameters do not have the same length, the
    function will return an empty list.

    Parameters
    ----------
    lst1 : non empty list of integers
        
    lst2 : non empty list of integers
        

    Returns
    -------
    newLst: a new list considering the rules described above
            or an empty list if the parameters have a
            different length

    '''
    

def generateListPrime(lst):
    '''
    From the parameter lst, generate a new list containing the numbers of lst
    that are prime numbers. Prime numbers are numbers greater than 1. 
    They only have two factors, 1 and the number itself. 
    This means these numbers cannot be divided by any number other than 1
    and the number itself without leaving a remainder.

    Parameters
    ----------
    lst : list
        list of positive integer numbers.

    Returns
    -------
    A new list containing only the prime numbers presented in the lst parameter

    '''
    

def main():
    print("Making the calls of the implemented methods")
    
    #call the method generateListPrime
    #if the method return an empty list you need to print
    #"No prime number in the list"
    #if the list returned is not empty you will print the list
    #that was returned
    
    
    #call the method generatingNewList
    #if the method returns an empty list you need to print
    #"Not possible to generate the new list"
    #if the list returned is not empty, print the list
    #that was returned
    
    

if __name__ == "__main__":
    main()
