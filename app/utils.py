import random

def weighted_choice(options):
    # Return a value based on weighted random selection
    total = sum(weight for item, weight in options)
    r = random.uniform(0, total)
    upto = 0
    for item, weight in options:
        if upto + weight >= r:
            return item
        upto += weight
