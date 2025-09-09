if __name__ == '__main__':
    N = int(input()) # line ka input
    data = list()   # empty list
    for i in range(N):
        s=input().split()
        if s[0] == "print":
            print(data)
        else:
            cmd = f"data.{s[0]}({', '.join(s[1:])})"
            eval(cmd)
