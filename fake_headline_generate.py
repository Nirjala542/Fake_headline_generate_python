import random
subjects=["Scientists", "Researchers", "Experts", "Analysts", "Developers"]
verbs=["discover", "analyze", "create", "investigate", "develop"]
objects=["new technologies", "innovative solutions", "groundbreaking methods", "cutting-edge tools", "revolutionary approaches"]
adjectives=["groundbreaking", "innovative", "revolutionary", "cutting-edge", "pioneering"]

# def generate_headline():
#     subject = random.choice(subjects)
#     verb = random.choice(verbs)
#     obj = random.choice(objects)
#     adj = random.choice(adjectives)
#     return  {subject} {verb} {adj} {obj}"

while True:
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    adj = random.choice(adjectives)
    headline = f" breaking news: {subject} {verb} {adj} {obj}"
    print(headline)

    user_input = input("Generate another headline? (y/n): ").strip()
    if user_input.lower() != 'y':
        break
print("thanks for using the fake headline generator. have a great day!")