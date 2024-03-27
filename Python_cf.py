# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

letter = input("Please enter a letter from the alphabet (a-z or A-Z): ")
vowels = ['a','e','i','o','u']
if letter.lower() in vowels:
    print ("The letter " + letter +" is a vowel.")
else:
    print("The letter "+ letter +" is a consonant")




# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

letter ='default'
while letter != 'quit':
  letter = input("Please enter a word or a phrase: ")
  if letter !='quit':
    length = len(letter)
    print(f"What you entered is {length} characters long")
print('Exiting the loop') 








# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

age = int(input("Input a dog's age: "))
if age<=2:
    dog_age = 10*age
    
else:
    dog_age = 20+(age-2)*7
print(f"The dog's age in dog years is {dog_age}")





# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


a = int(input("Enter the lengths of three side of a triangle: \na:"))
b = int(input("b: "))
c = int(input("c: "))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
      triType = 'equilateral'
    if a!=b !=c:
      triType = 'scalene' 
    else:
      triType = 'isosceles'


print(f'A triangle with sides of {a}, {b} & {c} is a {triType} triangle ')



# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):
fn = 0 #first number
sn = 1 #second number
#print term 0
print(f"term: 0 / number: {fn}")
for n in range(1,50):
    #get print number
    pn = fn + sn
    print(f"term: {n} / number: {pn}")
    fn,sn = sn, pn





# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.


Month = input("Enter the month of the year ")
day = int(input ("Enter the day of the year "))
if Month in ('Jan', 'Feb'):
    season = 'Winter'
if Month == 'Mar':
    if day<20:
        season = 'Winter'
    else:
        season = 'Spring'

if Month in ('Apr', 'May'):
    season = 'Spring'
if Month == 'June':
    if day<20:
        season = 'Spring'
    else:
        season = 'Summer'

if Month in ('July', 'Aug'):
    season = 'Summer'
if Month == 'Sep':
    if day<20:
        season = 'Summer'
    else:
        season = 'Autumn'

if Month in ('Oct', 'Nov'):
    season = 'Autumn'
if Month == 'Dec':
    if day<20:
        season = 'Autumn'
    else:
        season = 'Winter'

print(f"{Month} {day} is in {season}")
