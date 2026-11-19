# var = lambda arg: #str

#sot= lambda a,b,c: a+b+c
#print(sot(10,20,30))


#gst = lambda price: price+price*0.18
#print(gst(1000))

#avg=lambda l:sum(l)/len(l)
#l=[99,87,89,6,43]
#print(avg(l))

#iseven = lambda n :"Even" if n%2==0 else "odd"
#print(iseven(10))
#print(iseven(4))


#isvowel = lambda ch: "vowel" if ch in ' aeiouAEIOU' else "consonant"
#print(isvowel('a'))
#print(isvowel('z'))



#check = lambda data,pro: (f"product prices: {data[pro]['price']}" if data[pro]['stock']>0 else "Out of stock") if pro in data else "product is unavaliable"

#data = {
#    'apple':{'stock':10,'price':50},
#    'mango':{'stock':20,'price':40},
#    'sapota':{'stock':0,'price':30},
#    'coconut':{'stock':30,'price':120},
#        }

#print(check(data,'sapota')) 


#def addten(l):
#    for i in range(len(l)):
#        l[i]+=10
#    return l

#l = [9,2,4,34,5,45,54,2]
#print(addten(l))

#def domain(d):
#    for i in range(len(d)):
#        d[i] = (d[i].split('@')[1]).split('.')[0]
#    return d

#d =['xyz@codegnan.com','abc@gmail.com','pqr@yahoo.com']
#print(domain(d))


#l = [9,2,4,34,5,45,54,2]
#addten =list(map(lambda i:i+10 , l))
#print(addten)


#d = ['xyz@codegnan.com','abc@gmail.com','pqr@yahoo.com']
#domain = list(map(lambda i: i.split('@')[1].split('.')[0], d))
#print(domain)

# = ['saft','fahhh','gayyyy','yahoooo']
#cu = list(map(lambda i:i.upper(),c))
#print(cu)

#d = {'a':20,'b':30,'c':10000,'d':200000,'e':500000,}
#gst = list(map(lambda i:i,d.items()))
#print(d)


# = {'a':20,'b':30,'c':10000,'d':50000,'e':2000,}
#gst = dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
#print(gst)


#l = [1,2,3,4,5,66,67,56,7,34]
#even = list(filter(lambda i: i % 2 == 0, l))

#print(even)
#print(even)

#a = ['a','e','i','o','d','k','j','l']
#vowel = list(filter(lambda i: i in 'aeiouAEIOU', a))
#print(vowel)

#from functools import reduce

#l = [1,2,3,4,5,6,7]
#sumofl = reduce(lambda sum,i:sum+i,l)

#print(sumofl)

#l = [1,2,3,4,5,6,7]
#sumofl = reduce(lambda sum,i:sum*i,l)

#print(sumofl)

#l = [1,2,3,4,5,6,7]
#sumofl = reduce(lambda max,i:max if max>i else i,l)

#print(sumofl)

#l = [1,2,3,4,5,6,7]
#sumofl = reduce(lambda min,i:min if min>i else i,l)

#print(sumofl)
