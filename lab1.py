import math

a = 1 
c, d = map(int, input().split()) 

def func(a, c, d):
    if c < 0 or a * d + math.sqrt(c) <= 0:
        return "no value"
    else:
        return math.sin(a) / math.sqrt(a * d + math.sqrt(c)) + math.exp(2 * c + a) * (math.sin(c) ** 4)

print((func(a, c, d)))
