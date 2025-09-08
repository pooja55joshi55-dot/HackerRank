if __name__ =='__main__':
    data = int(input().strip())
    verify = data % 2
    if verify == 0 and (data < 5 or data > 20):
        print("Not Weird")
    elif (verify == 0 and  6<= data <= 20) or verify == 1:
        print("Weird")
