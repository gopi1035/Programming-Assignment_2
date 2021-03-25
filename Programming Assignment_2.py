#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Write a Python program to convert kilometers to miles?
kilo = int(input("Please enter the lenght in Kilometer "))
miles = kilo*0.621371
miles = round(miles,2)
print("Lenght {} miles ".format(miles))


# In[22]:


#Write a Python program to convert Celsius to Fahrenheit?
c= int(input("Enter the temperature in Celsius "))
f = (c * (9/5)) + 32
f= (round(f,2))
print("Temperature {} Fahrenheit.".format(f))


# In[30]:


#Write a Python program to display calendar?
#Unaware of solution, taken help from internet
import calendar
yy = int(input("Enter year(eg 2000,2001 etc): "))
mm = int(input("Enter month (eg 1,2,3 etc): "))
print(calendar.month(yy, mm))


# In[6]:


#Write a Python program to solve quadratic equation?
#Unaware of solution, taken help from internet
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))   
d = (b**2) - (4*a*c) 
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))


# In[7]:


#Write a Python program to swap two variables without temp variable?
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)
 


# In[ ]:




