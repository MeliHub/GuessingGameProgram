# This is small guessing game using while loops
#Melikaya Matiwane

covid_year = 2019
guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess = int(input('Guess the year corona virus started: '))
    guess_count += 1
    if guess == covid_year:
        print('You Won!')
        break
else:
    print('You made three guesses and failed')



