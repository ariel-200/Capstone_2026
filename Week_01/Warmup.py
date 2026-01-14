import datetime
from operator import length_hint

# Ask user for name
name = input('What is your name? ')

# Ask user for birthday month
month = int(input('What is the number of your birthday month? '))

# Print Name
print(f'Hello {name}!')

# How many letters in the user's name?
letters = len(name)
print(f'There are {letters} letters in your name.')

# Get date today
today = datetime.date.today()

# Print 'Happy Birthday' if birthday is current month
if month == today.month:
    print('Happy Birthday!')
else :
    print('Sorry, it\'s not your birthday yet.')





