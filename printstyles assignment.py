
# print ("Sales %10s, Total %10.3f" %("wrong", 4.34543)) # printf style formatting data

# # %10s >       1332

# print("Sales :{0:10d}, Total :{1:9.2f}".format(12323, 00.5467)) # padding spaces before for an integer(d)

# print ("{a:20} {b:30} and {c:s}".format(c = "Python", b = "Data Science", a = "ML")) # invalid statement; cannot assignment to integer;

# print ("{0:5d}, {1:} and {2:}".format(323, "Data Science", "ML"))

# print ("{a:10s} {b:20s} and {c:1.20s} {d:1.6f}".format(a = "Python", b = "Data Science", c = "ML", d = 32.3)) # padding spaces after a string for a String value(s) and sign not allowed for string formatter.


# # print ("passcode {0[pass]:10d} and authentication {1[auth]: 20d}".format({"pass": 3232}, {'auth': True})) # dict way print formats; int: before padding; str: after padding

# data = dict(x = 10, y = "why", z = 30);

# print ("Give values are, x is {x}, y is {y:}, z is {z}".format (**data)) # dict data print format
# a = 1,"you"
# print("{}".format(a))
# print ("{} {} {} {} {}".format(1,2,56.,5,"b77",7,6,697,3))

# string = "Python Programming";

# print (string.center(40, "-")) # Arranging string in exact 40 spaces and filled with "-"

# print (len("-----------Python Programming-----------"))

# print (string.ljust(20, '-')) # printing left aligned string with spaced filled with "-" symbol

# print (string.rjust(20, "*")); # print right aligned string with spaces covered with "*" symbol


# print ("phone : %d, %d%d" %(23, 23,55)) # formatting printf style string... 

# print ("phone : %32f" %9378348255.893)

# # # sample program

# t = (10,20,30,40,50,60)
# print(t)
# count = 0
# for i in t:
# 	print("t[%d] = %d"%(count, i)) # printf sytle formatting
# 	count = count +1


# # # sample program 2

# s = ['a','b','c','d']
# l = [1,2,3,4]

# print ({print ("d[%s] : % 2d"%(each, one), end = '; ') for each, one in zip(s,l)})

# # # sample 3

# mylist = [1,2,3]
# print("A list: %s" % mylist)

# # # sample 4

# # name = "John"
# # print("Hello, %s!" % name)

# # #===============

# # name = "John"
# # age = 23
# # print("%s is %d years old." % (name, age))

# # #Sample 5

# # data = ("John", "Doe", 53.44)
# # format_string = "Hello"

# # #print(format_string % data) # error; not all arguments converted into string; tuple is immutable object so cannot be convertable into string value.

# print (globals())

