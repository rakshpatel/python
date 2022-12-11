"""
Input: You are given array of integers and a SUM.
Output: Return True or False if there is any Subset for which elements adds up to given SUM

E.g.
Input:
    Array: 1 3 2 8 7
    Sum: 11
Output:
    True({3,8})
"""
from pprint import pprint
def subSetSum(array, sm, size):
    if sm == 0:
        return True

    if size == 0:
        return False

    m = [[None for _ in range(sm+1)] for _ in range(size + 1)]
    
    # pprint(m)
    for i in range(sm+1):
        m[0][i] = False
    
    for i in range(size + 1):
        m[i][0] = True

    # pprint(m)
    for i in range(1, size + 1):
        for j in range(1, sm + 1):
            if array[i-1] <= j:
                m[i][j] = m[i-1][j-array[i-1]] or m[i-1][j]
            else:
                 m[i][j] = m[i-1][j]
    return m[size][sm]

def main(exec="All", extraParam=None):
    inputDict = {
        1: {
            "Array": [1, 3, 4, 5],
            "Sum": 7
        },
        2:{
            "Array": [1, 3, 4, 5],
            "Sum": 6
        },
        3: {
            "Array": [1, 3, 4, 5],
            "Sum": 0
        },
        4: {
            "Array": [],
            "Sum": 7
        },
        5: {
            "Array": [1, 3, 4, 5],
            "Sum": 13
        },
        6: {
            "Array": [1, 3, 4, 13],
            "Sum": 13
        },
        7: {
            "Array": [1, 3, 4, 7],
            "Sum": 7
        }

    }
    if exec == "All":
        for key, val in inputDict.items():
            array = inputDict[key]["Array"]
            sm = inputDict[key]["Sum"]
            size = len(array)
            print("Test Case: {}".format(key))
            print("Input \nArray: {}\nSum: {}\nArraySize: {}".format(array, sm, size))
            print()
            
            subSetFound = subSetSum(array, sm, size)
            
            print("Is it possible?: {}".format(subSetFound))
            print("*"*20)
    elif exec == "List":
        for key in extraParam:
            array = inputDict[key]["Array"]
            sm = inputDict[key]["Sum"]
            size = len(array)
            print("Test Case: {}".format(key))
            print("Input \nArray: {}\nSum: {}\nArraySize: {}".format(array, sm, size))
            print()
            
            subSetFound = subSetSum(array, sm, size)
            
            print("Is it possible?: {}".format(subSetFound))
            print("*"*20)
    elif exec == "One":
        key = extraParam
        array = inputDict[key]["Array"]
        sm = inputDict[key]["Sum"]
        size = len(array)
        print("Test Case: {}".format(key))
        print("Input \nArray: {}\nSum: {}\nArraySize: {}".format(array, sm, size))
        print()
        
        subSetFound = subSetSum(array, sm, size)
        
        print("Is it possible?: {}".format(subSetFound))
        print("*"*20)

if __name__ == "__main__":
    main()
    # main(exec="One", extraParam=5)
    # main(exec="List", extraParam=[2, 5])