#To find the largest palindrome made from product of 3-digit numbers
a=[]
product=[]
dic={}
l=list(range(100,1000))
print("Total three digits numbers",l)
for i in range(900):
	j=i
	for j in range(900):
		w=l[i]*l[j]
		dic.update({w:{l[i],l[j]}})
		product.append(w)
	
		

def isPalindrome(s):
    s = str(s)
    return s == s[::-1]


tmlst=[]
for i in range(len(product)):
	if isPalindrome(product[i]):
		tmlst.append(product[i])
		
print("The palindrome is",tmlst)
print("The Highest Palindrome is",max(tmlst))
print ("The palindrome is product of",dic[max(tmlst)])

