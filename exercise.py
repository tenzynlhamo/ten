age = int(input('Enter your age:'))
std = input('Are you student? ')
eligible = (age <= 12) or (age >=13 and age <=18 and std == 'yes')

if eligible:
    print('You are eligible for a discount on the movie ticket')

else :
    print('You are not eligible for a discount on the movie ticket')
