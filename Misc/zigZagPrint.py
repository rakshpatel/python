def collatzFun(n):
    global cnt
    if n == 1:
        return cnt
    
    if n % 2 == 0:
        cnt += collatzFun(int(n/2))
    else:
        cnt +=  collatzFun(int(3*n+1))
    
    return cnt


if __name__ == "__main__":
    cnt = 0
    collatzFun(2)
    print(cnt)
    cnt = 0
    collatzFun(5)
    print(cnt)