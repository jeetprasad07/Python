def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n


num =int(input("Enter a number : "))
print ("sum :",cal_sum(num))