#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[2]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[3]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[4]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[6]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[7]:


a = int(input("enter first number: "))
b = int(input("enter second number: "))
 
sum = a + b
 
print("sum:", sum)


# In[8]:


print("Enter the marks of five subjects::")

subject_1 = float (input ())
subject_2 = float (input ())
subject_3 = float (input ())
subject_4 = float (input ())
subject_5 = float (input ())

total, average, percentage, grade = None, None, None, None

total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average = total / 5.0
percentage = (total / 500.0) * 100

if average >= 90:
    grade = 'A'
elif average >= 80 and average < 90:
    grade = 'B'
elif average >= 70 and average < 80:
    grade = 'C'
elif average >= 60 and average < 70:
    grade = 'D'
else:
    grade = 'E'

print ("\nThe Total marks is:   \t", total, "/ 500.00")
print ("\nThe Average marks is: \t", average)
print ("\nThe Percentage is:    \t", percentage, "%")
print ("\nThe Grade is:         \t", grade)


# In[11]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[12]:


ListName = ["Hello", "Edureka", 1, 2, 3]
print ("Number of items in the list = ", len(ListName))


# In[13]:


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


# In[15]:


def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([3, 10, -8, 5]))


# In[18]:


def printValues():
	l = list()
	for i in range(1,20):
		l.append(i**2)
	print(l[5:])
printValues()


# In[ ]:




