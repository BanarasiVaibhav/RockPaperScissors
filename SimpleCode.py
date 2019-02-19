print('.....Rock.....')
print('.....Paper.....')
print('.....Scissor.....')

player1=input('Player1....Enter your move....     ')
print('******** No Cheating  *********')
print('')
print('******** No Cheating  *********')
print('')
print('')
print('')
print('******** No Cheating  *********')

print('')
print('******** No Cheating  *********')
print('')
print('')
print('******** No Cheating  *********')
print('')
print('******** No Cheating  *********')
print('')
print('')
print('')
print('******** No Cheating  *********')

print('')
print('******** No Cheating  *********')
print('')
print('')
print('******** No Cheating  *********')
print('')
print('******** No Cheating  *********')
print('')
print('')
print('')
print('******** No Cheating  *********')

print('')
print('******** No Cheating  *********')
print('')
print('')
print('******** No Cheating  *********')
print('')
print('******** No Cheating  *********')
print('')
print('')
print('')
print('******** No Cheating  *********')

print('')
print('******** No Cheating  *********')
print('')
print('')
player2=input('Player2....Enter your move....     ')

# player1 == rock
if player1=='rock' and player2=='scissors':
    print('')
    print('')
    print('Player 1 wins !')
elif player1=='rock' and player2=='paper':
    print('')
    print('')
    print('Player 2 wins !')


# player1 == scissors
elif player1=='scissors' and player2=='rock':
    print('')
    print('')
    print('Player 2 wins !')
elif player1=='scissors' and player2=='paper':
    print('')
    print('')
    print('Player 1 wins !')


# player1 == paper
elif player1=='paper' and player2=='rock':
    print('')
    print('')
    print('Player 1 wins !')
elif player1=='paper' and player2=='scissors':
    print('')
    print('')
    print('Player 2 wins !')

elif player1 == player2:
    print('')
    print('')
    print('ohh its a tie !')

else :
    print('')
    print('')
    print('')
    print('Invalid input')

