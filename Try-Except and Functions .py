print("Hello World!")

x = 23 % 4
print(x)


print(type("Hatay"))

a = 3
b = 4 

print(a+b)

a = 3
print(type(a))

print(float(99) + 100)

i = 42
print(type(i))

f = float(i)
print(f)

sval = '123'
print(type(sval))

ival = int(sval)
print(type(ival))

print(ival + 1)

##############################
nam = input('Who are you? ')
print('Welcome', nam)

sayi = input('Bir sayi giriniz: ')
print('Sayiniz ', sayi )
##############################

nam = input('Who are you? ')
print('Welcome', nam)

c = 2 
d = 6 
print(c**d)


inp = input('Europe floor?')
usf = int(inp) + 1 
print('US floor', usf)

# If statements:

x = 5 

if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

x = 5

if x > 2 :
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

x = 12

if x < 3 : 
    print('small')
elif x < 10 :
    print('Medium')
else:
    print('Large')

print('All Done')


x = 157

if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
elif x < 20 :
    print('Big')
elif x < 40 : 
    print('Large')
elif x < 100 : 
    print('Huge')
else :
    print('Ginormous')

# try and except commands:
# Thanks to these commands, continuity of the code is ensured even if there is an error.

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)


astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

######################################
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print('Nice Work')
else:
    print('Not a number')

######################################

# Functions:

def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

big = max('Hello world')
print(big)

tiny = min('Hello World')
print(tiny)


def greet(lang) :
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')


def greet():
    return 'Hello'

print(greet(), 'Glenn')
print(greet(), 'Sally')

