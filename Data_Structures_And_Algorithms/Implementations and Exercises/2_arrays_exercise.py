"""
Excercice 1:
Let us say your expense for every month are listed below,
	1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190
"""

month_expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(f'Feb extra month spent vs Jan {month_expenses[1] - month_expenses[0]}.') 

# 2. Find out your total expense in first quarter (first three months) of the year.

print(f'Total 1rst Quarter expense {sum(month_expenses[:2])}.')

# 3. Find out if you spent exactly 2000 dollars in any month

print(f'Is there any moth with an expense of 2000? Result: {2000 in month_expenses}.')

# 4. June month just finished and your expense is 1980 dollar.
# Add this item to our monthly expense list.

month_expenses.append(1980)
print(month_expenses)
# 5. You returned an item that you bought in a month of April and got a refund of 200$.
#  Make a correction to your monthly expense list based on this.

print(f'April expense b4 correction {month_expenses[4]}.')
month_expenses[3] = month_expenses[3] - 200

print(f'April expense after correction {month_expenses[4]}.')

# Excercice 2:
# You have a list of your favourite marvel super heros.


heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list

print(f'List lenght {len(heros)}')

# 2. Add 'black panther' at the end of this list.

heros.append('black panter')
print(f"2: {heros}")

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'.

heros.pop(-1)
heros.insert(heros.index('hulk') + 1, 'black panter')

print(f"3: {heros}")

# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.

heros[1:3] = ['doctor strange']
print(f"4: {heros}.")

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

print(f'5: {sorted(heros)}')

# Excercice 3:
# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function.

max_number = int(input('Provide an integer for max number: '))
if not isinstance(max_number, int):
    raise ValueError('models should be an integer')

odd_list = [odd for odd in range(1, max_number + 1) if odd % 2 != 0]
print(odd_list)
