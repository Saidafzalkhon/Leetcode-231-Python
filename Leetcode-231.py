if __name__ == "__main__":
    n = int(input())
    if (n&(n-1))==0 and n != 0:
        print(True)
    else: print(False)