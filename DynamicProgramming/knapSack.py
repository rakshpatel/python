# 0-1 knapSack
"""
We have two lists(arrays) available. One contains value of the items and other containse weight of the items. We have one bag with capacity `size`. 
Our aim is to maximize values while filling the up the bag.
"""
from pprint import pprint
def knapSack(weightList, valueList, weightBag, size):
    """
    Simple Recursive Approach
    """
    # Base condition
    if size == 0 or weightBag == 0:
        return 0
    
    # Choice diagram
    if weightList[size-1] <= weightBag:
        return max(valueList[size-1] + knapSack(weightList, valueList, weightBag-weightList[size-1], size - 1 ), knapSack(weightList, valueList, weightBag, size - 1 ))
    else:
        return knapSack(weightList, valueList, weightBag, size - 1)


def knapSackMinit(weightList, valueList, weightBag, size):
    """
    Memoization approach init
    """
    m = [[-1 for _ in range(weightBag+1)] for _ in range(size+1)]
    val = knapSackM(weightList, valueList, weightBag, size, m)
    #pprint(m)
    return val

def knapSackM(weightList, valueList, weightBag, size, m):
    """
    Memoization approach init: Recursive call
    """
    # Base condition
    if size == 0 or weightBag == 0:
        return 0
    if m[size][weightBag] != -1:
        print("Found")
        return m[size][weightBag]
    # Choice diagram
    if weightList[size-1] <= weightBag:
        m[size][weightBag] =  max(valueList[size-1] + knapSackM(weightList, valueList, weightBag-weightList[size-1], size - 1, m), knapSackM(weightList, valueList, weightBag, size - 1, m ))
    else:
        m[size][weightBag] = knapSackM(weightList, valueList, weightBag, size - 1, m)
    
    return m[size][weightBag]

def knapSackDP(weightList, valueList, weightBag, size):
    if size == 0 or weightBag == 0:
        return 0
    m = [[None for _ in range(weightBag + 1)] for _ in range(size+1)]
    # pprint(m)
    for i in range(size+1):
        m[i][0] = 0
    for i in range(weightBag + 1):
        m[0][i] = 0
    # pprint(m)
    for i in range(1, size+1):
        for j in range(1, weightBag + 1):
            if weightList[i-1] <= j:
                m[i][j] = max(valueList[i-1]+m[i-1][j-weightList[i-1]], m[i-1][j])
            else:
                m[i][j] = m[i-1][j]
    # pprint(m)
    return m[size][weightBag]


def main(exec="All", extraParam=None):
    inputDict = {
        1: {
            "weightList": [1, 3, 4, 5],
            "valueList":[1, 4, 5, 7],
            "weightBag": 7
        },
        2:{
            "weightList": [1, 3, 4, 5],
            "valueList":[1, 4, 5, 7],
            "weightBag": 6
        },
        3: {
            "weightList": [1, 3, 4, 5],
            "valueList":[1, 4, 5, 7],
            "weightBag": 0
        },
        4: {
            "weightList": [],
            "valueList":[],
            "weightBag": 7
        },
        5: {
            "weightList": [1, 3, 4, 5],
            "valueList":[1, 4, 5, 7],
            "weightBag": 13
        },
        6: {
            "weightList": [1, 3, 4, 13],
            "valueList":[1, 4, 5, 7],
            "weightBag": 13
        },
        7: {
            "weightList": [1, 3, 4, 7],
            "valueList":[1, 4, 5, 20],
            "weightBag": 7
        }

    }
    if exec == "All":
        for key, val in inputDict.items():
            weightList = inputDict[key]["weightList"]
            valueList = inputDict[key]["valueList"]
            weightBag = inputDict[key]["weightBag"]
            size = len(valueList)
            print("Test Case: {}".format(key))
            print("Input \nWeight List: {}\nValue List: {}\nBag Capacity: {}\nArraySize: {}".format(weightList, valueList, weightBag, size))
            print()
            
            maxValueR = knapSack(weightList, valueList, weightBag, len(valueList))
            maxValueM = knapSackMinit(weightList, valueList, weightBag, len(valueList))
            maxValueDP = knapSackDP(weightList, valueList, weightBag, len(valueList))
            
            print("Max Value Recursive: {}, Max Value Memoization: {}, Max Value DP:{}".format(maxValueR, maxValueM, maxValueDP))
            print("*"*20)
    elif exec == "List":
        for key in extraParam:
            weightList = inputDict[key]["weightList"]
            valueList = inputDict[key]["valueList"]
            weightBag = inputDict[key]["weightBag"]
            size = len(valueList)
            print("Test Case: {}".format(key))
            print("Input \nWeight List: {}\nValue List: {}\nBag Capacity: {}\nArraySize: {}".format(weightList, valueList, weightBag, size))
            print()
            maxValueR = knapSack(weightList, valueList, weightBag, len(valueList))
            maxValueM = knapSackMinit(weightList, valueList, weightBag, len(valueList))
            maxValueDP = knapSackDP(weightList, valueList, weightBag, len(valueList))
            
            print("Max Value Recursive: {}, Max Value Memoization: {}, Max Value DP:{}".format(maxValueR, maxValueM, maxValueDP))
            print("*"*20)
    elif exec == "One":
        key = extraParam
        weightList = inputDict[key]["weightList"]
        valueList = inputDict[key]["valueList"]
        weightBag = inputDict[key]["weightBag"]
        size = len(valueList)
        print("Test Case: {}".format(key))
        print("Input \nWeight List: {}\nValue List: {}\nBag Capacity: {}\nArraySize: {}".format(weightList, valueList, weightBag, size))
        print()
        maxValueR = knapSack(weightList, valueList, weightBag, len(valueList))
        maxValueM = knapSackMinit(weightList, valueList, weightBag, len(valueList))
        maxValueDP = knapSackDP(weightList, valueList, weightBag, len(valueList))
        
        print("Max Value Recursive: {}, Max Value Memoization: {}, Max Value DP:{}".format(maxValueR, maxValueM, maxValueDP))
        print("*"*20)

if __name__ == "__main__":
    main()
    # main(exec="One", extraParam=5)
    # main(exec="List", extraParam=[2, 5])
    
