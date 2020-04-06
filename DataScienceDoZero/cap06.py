import random
import math



girl = "girl"
boy = "boy"
def random_kid():
    return random.choice([boy, girl])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == girl:
        older_girl += 1
    if older == girl and younger ==girl:
        both_girls += 1
    if older == girl or younger == girl:
        either_girl += 1
print("P(both | older):", both_girls / older_girl)
print("P(both | either):", both_girls / either_girl)


def uniform_pdf(x):
    # Probability Density Function
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    # Retorna a probabilidade de uma variável aleatoria uniforme ser <= x
    if x < 0: return 0
    elif x< 1: return x
    else: return 1


def normal_pdf(x, mu=0, sigma=1);
    sqrt_two_pi = math.sqrt(2*math.pi)
    return (math.exp(-(x-mu)**2/2/sigma**2)/(sqrt_two_pi*sigma))

