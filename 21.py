from  random  import  randrange

player_sum = 0
diler_sum = 0
while True:
    print('You have', player_sum, 'points.')
    print('Diler has', diler_sum, 'points.')
    usermove = input('more card? y or n ')
    if usermove == 'y':
        card = randrange(2,11)
        print("You've got", card)
        player_sum = player_sum + card
        if player_sum > 21:
            break
    elif usermove == 'n':
        print(player_sum)
        break
    else:
        print('What?')
    dilcard = randrange(2,11)
    print('Diler has', dilcard)
    diler_sum = diler_sum + dilcard
    if diler_sum >= 19:
        break
    elif diler_sum > 21:
        break

if player_sum == 21:
    print('YEAH! You won!')
elif diler_sum == 21:
    print('Oh, Diler won!')
elif player_sum > 21 > diler_sum:
    print('Diler won!', player_sum, 'for you is on', player_sum - 21, 'points more than needed!')
elif diler_sum > 21 > player_sum:
    print('Player won!', diler_sum, 'for Diler is on', diler_sum - 21, 'points more than needed!')
elif player_sum < diler_sum < 21:
    print('Mhe Diler was better than you on', diler_sum - player_sum, 'points!')
elif 21 > player_sum > diler_sum:
    print('Wow, You were better than Diler on', player_sum - diler_sum, 'points!')