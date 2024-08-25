
'''def count_down(n):

    while n>0:
       print(n)
       n=n-1
count_down (10)


def sum_even_numbers(limit):
    sum=0
    for x in range(1,limit):
        if x%2==0:
            sum=sum+x
        else:
            continue
    print(sum)
sum_even_numbers(10)'''


def is_prime(n):
    if n<=1:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
   
    return True   
        
print(is_prime(7))


def factorial(n):
    factoriall=1
    for x in range(1,n+1):
        factoriall=factoriall*x
    print(factoriall)

factorial(4)







