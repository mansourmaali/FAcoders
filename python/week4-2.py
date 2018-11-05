print('Numbers from 1 to 10')
x=6
input('Guess the number:')
while int(input('Guess the number:'))!=x:
    if 1< int(input('Guess the number:'))<10:
        continue
    else:
        print(input('Guess the number:'))
        continue
else:
    print('Great you did it')
