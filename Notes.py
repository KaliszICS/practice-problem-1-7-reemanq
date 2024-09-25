'''
    Lesson: Booleans
    Author: Mr Kalisz
    Date Created: Sept 25, 2024
    Date Last Modified: Sept 25, 2024
'''

#Booleans - Have two values - True or False

bool1 = True
print(bool1)
bool1 = False
print(bool1)

#Comparison - <, > , ==(equivalence), != (non equivalence), >=, <=

bool1 = 10 < 5 #False
print(bool1)

bool1 = 6 > 6 #False
print(bool1)

bool1 = 6 >= 6 #True
print(bool1)

bool1 = 5 == 3 #False

bool1 = 3 != 5 #True

#Is it a negative number?
# num = int(input("Input a number: ")) #converts the input to an integer
# bool1 = num < 0 #
# print(bool1)

#bool1 = 5 < "word" #Runtime error -> can't compare str and int

bool1 = 5 == 5.0 #floats and integers can be compared
#floats and ints can be equal
print(bool1)

bool1 = "word" > "hello" #alphabetically compared KIND OF
print(bool1)

bool1 = "fire" < "firefighter" #True
#Compares character by character and proceeds if they are the same
#If one word ends and the other doesn't, that word is less than the other
print(bool1)

bool1 = "Zoo" > "alphabet" #letters are compared by their ASCII value
#https://www.asciitable.com/
print(bool1)

#Converting - bool()

# int-> bool

print(bool(5)) #True
print(bool(-5)) #True
print(bool(0)) #False

# float -> bool

print(bool(5.0)) #True
print(bool(-5.0)) #True
print(bool(0.0)) #False

# str -> bool

print(bool("True")) #True
print(bool("False")) #True
print(bool("Hello")) #True
print(bool("")) #False


