# Ex 1:

import re

with open ('nyc_weather.csv') as f:
    weather = []
    f.readline()
    for line in f:
        token = line.split(',')
        weather.append(int(token[1]))

print(f'Mean : {sum(weather)/len(weather)}.')

print(f'Max temperature first 10 days: {max(weather[:10])}.')

# Ex 2:

with open ('nyc_weather.csv') as f:
    weather = {}
    f.readline()
    for line in f:
        token = line.split(',')
        weather[token[0]] = int(token[1])

print(f'Temperature Jan 9: {weather["Jan 9"]}.')
print(f'Temperature Jan 9: {weather["Jan 4"]}.')

# Ex 3:
with open ('poem.txt') as f:
    poem = {}
    for line in f:
        for word in line.split(' '):
            word = re.sub(r'[^a-zA-Z]', '', word)
            if word in poem:
                poem[word] += 1
            else:
                poem[word] = 1

print(poem)