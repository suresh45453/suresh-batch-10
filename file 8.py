def profile(name, age, place):
    txt = "My name is {}. I am {} years old. I am from {}."
    print(txt.format(name, age, place))
profile("Suresh", 21,"KSRM")
# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement
def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("Not palindrome")
a = int(input("enter the value: "))
palindrome(a)
#? Based on the declaration of parameter

#? functions are divided into 5 catagories

# postal args
# keywords args
# defalt args
# variable length args
# keyword variable length args

# * Positional args
#Eg:1;
##def profile(name, phone, mark):
##    txt ="My name is {}. My phone number is {}. I got {} marks."
##    print(txt.format(name, phone, mark))
##
##    profile(9704984013, "mani", 92)
# * Keyword args
# ! Eg:1
#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(name="Usman",mark=100,phone=96668686)
# * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "suresh", mark=99, phone=9876543210) # Error
# profile(9876543210,name= "suresh", mark=99) # error
profile("suresh",mark=98,phone=9876543210)
# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("Shashank",9876543210)
# ---> Keyword variable length args
# kwargs --> Which is used to provide the args in the form of key
#            value pair.
# Eg:-1
'''
def price(**price_list):
    print(price_list)
price(shirt = 1000, iphone = 800000)    
'''
# Eg:-2
'#'
d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200,) 
# ? eg:4
class person1:
    frame = "malli" # attribute or static variable
    lname = "T"

    def first_name(person):
        print(person.frame)

    def full_name(person):
        print(person.frame+" " +person.lname)

p = person1()
p.first_name()
p.full_name()
