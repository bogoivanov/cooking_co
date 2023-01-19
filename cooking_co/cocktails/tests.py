import random

# Create a list of participants
participants=[]
for i in range(0,10):
    participants.append(f'"NAME{i}"')

# Shuffle the list of participants
random.shuffle(participants)

# Assign each participant a secret santa
secret_santas = {}
for i in range(len(participants)):
    secret_santas[participants[i]] = participants[(i + 1) % len(participants)]

# Print out the secret santa assignments
for participant, secret_santa in secret_santas.items():
    print(f"{participant}'s secret santa is {secret_santa}")
