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

#res = {i for i in range(1,11)}
#print(res)

#n =16
#fact ={i for i in range (1,n+1)if n%i==0}
#print(fact)


