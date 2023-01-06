# Python Quiz

print('Welcome to my Quiz game.')

score = 0
playing = input('Do you want to play😃 ? ')
if playing == 'Yes'.lower():
    print('Lets get started.')
else:
    print('Goodbye')

Question_1 = input('What does CPU stand for? ')
if Question_1 == 'Central Processing Unit'.lower():
    print('Correct')
    score = score + 1
else:
    print('Incorrect')
    score = score - 1

Question_2 = input('What does GPU stand for? ')
if Question_2 == 'Graphics Processing Unit'.lower():
    print('Correct')
    score = score + 1
else:
    print('Incorrect')
    score = score - 1

print('congrats you scored ' + str(score) + ' points')
