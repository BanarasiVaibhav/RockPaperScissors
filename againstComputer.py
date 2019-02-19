import random
print('.....Rock.....')
print('.....Paper.....')
print('.....Scissor.....')

player1=input('Player1....Enter your move....     ')
player1=player1.lower()
number=random.randint(0,1000)
computer=''

if number%3==0:
    computer = 'scissors'
    print('')
    print("computer chose " + str(computer))

elif number%3==1:
    computer='rock'
    print('')
    print("computer chose " + str(computer))

elif number%3==2:
    computer='paper'
    print('')
    print("computer chose "+ str(computer))



# player1 == rock
if player1=='rock' and computer=='scissors':
    print('')
    print('')
    print('Player 1 wins !')
elif player1=='rock' and computer=='paper':
    print('')
    print('')
    print('computer wins !')


    # player1 == scissors
elif player1=='scissors' and computer=='rock':
    print('')
    print('')
    print('computer wins !')
elif player1=='scissors' and computer=='paper':
    print('')
    print('')
    print('Congratulations You won !')


    # player1 == paper
elif player1=='paper' and computer=='rock':
    print('')
    print('')
    print('Congratulations You won !')
elif player1=='paper' and computer=='scissors':
    print('')
    print('')
    print('computer wins !')

elif player1 == computer:
    print('')
    print('')
    print('ohh its a tie !')

else :
    print('')
    print('')
    print('')
    print('Invalid input')
