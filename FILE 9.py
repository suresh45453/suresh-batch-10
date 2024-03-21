# s1 = "Hello how are you"
# s2="Hello how is"
s1=s1.split(" ")
s2=s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)



#3.) Wrire a code print the 8th fibanochi number
#0,1,1,2,3,5,8

# n1 = 0
# n2 = 1
# ans = 0+1 ==> 1

# n1 = 1
# n2 = 1
# ans = 1+1 ==> 2

# n1 = 1
# n2 = 2
# ans = 1+2 ==> 3

# n1 = 2
# n2 = 3
# ans = 2+3=5


# ! find the 8th fibanochi number
# num = 8
# n1 = 0
# n2 = 1

# for val in range(num):
#     ans = n1+n2
#     n1 = n2
#     n2 = ans
# print(ans)
# eg:6
# to use the variables inside the constructor in another methods
class class1:
    def __init__(self):
        self.name = "malli"
        self.email = "malli@gmail.com"
        # return name, email # error --> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()


# ! Eg:2
'''
class c1:
    def __init__(self):
        print("Iam constructor from parent class")

class child1(c1):
    pass

obj = child1()
'''



# hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6:
    def m6(self):
        print("Class 6")
# * Ploymorphism in operators
#-----> +
# print(8+8)
# print("k"+'l')
# print([1,2,3]+[4,5,6])

# *
# print(6*7)
# l1 = [1,2,3,4]
# print(*l1)
# def f1(*args)
# l1= [1,2,3,4]
# print(l1*10)

# polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading
# 2.) Method overriding
