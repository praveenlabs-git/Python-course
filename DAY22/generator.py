'''
def reels():
    res = ('1-100','101-200','201-300','301-400','401-500','501-600','601-700')
    yield res[0]
    yield res[1]
    yield res[2]
    yield res[3]
    yield res[4]
    yield res[5]
    yield res[6]

feed =reels()
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
'''

#def reels():
#    res = ('1-100','101-200','201-300','301-400','401-500','501-600','601-700')
#    for i in res:
#        yield i

#feed = reels()
#for i in feed:
#    print(i)


#def factors(n):
#    for i in range(1,n+1):
#        if n%2==0:
#            yield i

#res = factors(18)
#for i in res:
#    print(i)


#def prime_numbers(n):
#    for i in range(2, n + 1):
#        for j in range(2, i):
#            if i % j == 0:
#                break
#        else:
#            yield i

#res = prime_numbers(100)

#for i in res:
#    print(i)


#n =20

#a=0
#b=1
##for i in range(n-2):
#   c = a+b
#    print(c)
#    a = b
#    b = c

'''
def fibonacci(n):
    a = 0
    b = 1

    yield a
    yield b

    for i in range(n-2):
        c = a + b
        yield c

        a = b
        b = c

res = fibonacci(20)

for i in res:
    print(i)

'''


#def fib(n):
#    if n==1:
#        yield 0
#    elif n >=2:
#        a,b=0,1
#        yield a
#        yield b
#        for i in range(n-2):
#            c = a+b
#            a = b
#            b = c
#            yield c

#res = fib(4)
#for i in res:
#    print(i)

'''
res = [i for i in range(1,11)]
print(res)

n =16
fact =[i for i in range (1,n+1)if n%i==0]
print(fact)

names = ['praveen','harsh','prashanth','pavan']
resn = [i for i in names if i.startswith('p')]
print(resn)

l = [1,2,3,4,5,6,76,34,86,41,43,67,97,]
rese = [i if i%2==0 else 0 for i  in l]
print(rese)

nes = [[j for j in range (1,4)] for i in range(5)]
print(nes)
'''
