#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 10
while n >= 0:
    print(n)
    n=n-1


# In[3]:


n=1
s=0
while n<=100:
    if n%3==0:
        s=s+n
        n=n+1
    else:
        n=n+1
print(s)


# In[5]:


n=1
s=0
while n<=100:
    if n%3==0:
        s=s+n
    n+=1
print(s)


# In[6]:


math=[60,90,70,70,100]
j=1
for i in math:
    if i >=90:
        print(j,"번째 학생은 합격")
    else:
        print(j,"번째 학생은 불합격")
    j+=1


# In[10]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i%2==0:
        print(i)


# In[13]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i%2!=0:
        continue
    print(i)


# In[15]:


print(range(11))


# In[18]:


for i in range(1,11):
    print(i)


# In[42]:


for i in range(2,10):
    for j in range(1,10):
        if j==1:
            print(i,"단")
        print(i*j,end="\t")
        if j==9:
            print("\n")


# In[46]:


s=0
for i in range(0,101,2):
    s=s+i
print(s)


# In[54]:


list1=[1,2,3,4]
print(list1)

list2=[num for num in list1]
print(list2)

list3=[num*2 for num in list1]
print(list3)

list4=[num*2 for num in list1  if num%2==0]
print(list4)


# In[69]:


no=80
if no >=80:
    print("합격")
else:
    print("불합격")
    
print("합격" if no>=90 else "불합격")

