import random

randomInteger = random.randint(1, 10)
print(randomInteger)

randomFloat = random.random() * 5
print(randomFloat)

val = random.randint(0, 1)
if val == 0:
    print("Heads")
else:
    print("Tails")


# Lists

states_of_america = [
    'Alabama',
    'Alaska',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky[D]',
    'Louisiana',
    'Maine',
    'Maryland',
    'Massachusetts[D]',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania[D]',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virginia[D]',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming'
]

#states_of_america.extend(["Angelaland", "Jack Bauer land"])

# top = len(states_of_america) - 1
# print(states_of_america[random.randint(0, top)])

print(random.choice(states_of_america))

#print(states_of_america)
