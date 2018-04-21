import random
overlap = [number for number in random.sample(range(100), random.randint(1, 99)) if number in random.sample(range(100), random.randint(1, 99))]
print(overlap)