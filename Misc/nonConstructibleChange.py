def nonConstructibleChange(coins):
    # Write your code here.
    if not coins or min(coins) != 1:
        return 1
  
        
    coins.sort() # nlog(n)
    for val in range(coins[0], sum(coins)+1):
        
        if not canCreate(val, coins):
            return val
    return sum(coins)+1

#2**n
def canCreate(val, coins): 
    if val == 0:
        return True
    if not coins:
        return False
    return canCreate(val-coins[0], coins[1:]) or canCreate(val, coins[1:])

if __name__ == "__main__":
    coins = [1, 2, 4, 7]
    print(nonConstructibleChange(coins))