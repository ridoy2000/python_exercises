import random


rand_num = random.randint(1, 10) #integer
rand_nu2 = random.uniform(1, 10) #floating

print(rand_num)
print(rand_nu2)

random_number3 = random.randint(0,1)

if random_number3 == 1:
    print("heads")
else:
    print("tails")
