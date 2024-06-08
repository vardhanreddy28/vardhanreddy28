def isarmstrongnumber(num):
    def powersum(n, power):
        if n==0:
            return 0
        return (n%10)**power+powersum(n//10, power)
    numstr=str(num)
    power=len(numstr)
    return num == powersum(num, power)
print(isarmstrongnumber(153))  
print(isarmstrongnumber(123))  
