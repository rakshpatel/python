"""
Input: You are given array of integers.
Output: Return True or False if you can divide an array into two subset, both of which has the same sum

E.g.
Input:
    Array: 1 5 11 5
Output:
    True({1, 5, 5}, {11})
"""
from subSetSum import subSetSum
def equalSumPartition(array, size):
    sm = sum(array)
    if sm % 2 != 0:
        return False
    
    return subSetSum(array, int(sm/2), size)



def main(exec="All", extraParam=None):
    inputDict = {
        1: {
            "Array": [1, 3, 4, 5],
        },
        2:{
            "Array": [1, 5, 11, 5],
        },
        3: {
            "Array": [1, 2, 3, 4, 10]
        }

    }

    if exec == "All":
        for key, val in inputDict.items():
            array = inputDict[key]["Array"]
            size = len(array)
            print("Test Case: {}".format(key))
            print("Input \nArray: {}\nArraySize: {}".format(array, size))
            print()
            
            equalSumPartitionFound = equalSumPartition(array, size)
            
            print("Is it possible?: {}".format(equalSumPartitionFound))
            print("*"*20)
    elif exec == "List":
        for key in extraParam:
            array = inputDict[key]["Array"]
            size = len(array)
            print("Test Case: {}".format(key))
            print("Input \nArray: {}\nArraySize: {}".format(array, size))
            print()
            
            equalSumPartitionFound = equalSumPartition(array, size)
            
            print("Is it possible?: {}".format(equalSumPartitionFound))
            print("*"*20)
    elif exec == "One":
        key = extraParam
        array = inputDict[key]["Array"]
        size = len(array)
        print("Test Case: {}".format(key))
        print("Input \nArray: {}\nArraySize: {}".format(array, size))
        print()
        
        equalSumPartitionFound = equalSumPartition(array, size)
        
        print("Is it possible?: {}".format(equalSumPartitionFound))
        print("*"*20)


if __name__ == "__main__":
    main()
    # main(exec="One", extraParam=5)
    # main(exec="List", extraParam=[2, 5])