#!/usr/bin/python3

print('hello my name is Luc')

print('i will draw you a dinosour')
print('''
               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|
''')

# I will be my_age years old this year, when was I born? Write the forumlar
# this_year - my_age =
# 2018 - 9 = 2009
# 2018 - 2009 = 9
# 2018 - 9 = 2009
# 2009 + 9 = 2018
# 9 + 2009 = 2018

# 1 + 1 = 2
# 2 = 2

#10 20 30
#
#10 + 20 = 30
#30 = 10 + 20
#10 = 30 - 20
#20 = 30 - 10

#age     this_year    birth_year
#9       2018         2009
#
#this_year = age + birth_year
#2018 = 9 + 2009
#age = this_year - birth_year
#9 = 2018 - 2009
#birth_year = this_year - age
#2009 = 2018 - 9
#
#
#user_age    this_year    user_birth_year
#this_year = user_age + user_birth_year
#user_age = this_year - uaer_birth_year
#user_birth_year = this_year - user_age

# Now it's 2018, I was born in 2009, what's my age?
# 2018 - 2009 = my_age
# my_age = 2018 - 2009
this_year = 2019
birth_year = 2009
my_age = this_year - birth_year

print('I am ' + str(my_age) + ' years old')

# Print out the user's age
user_age = input('How old are you?')
print('you are ' + user_age + ' years old')
# Now that we know how old the user is this year, calculate the user's birth year and print it out.
# this_year - user_age =
user_birth_year = this_year - int(user_age)
print('your birth year is ' + str(user_birth_year))
