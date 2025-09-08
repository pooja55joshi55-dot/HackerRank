def is_leap(year):
    if (year%4==0 and year%100 !=0 ) or (year%400 ==0):
        return True
    return False

if __name__ =='__main__':
    year = int(input().strip())
    print(is_leap(year))
