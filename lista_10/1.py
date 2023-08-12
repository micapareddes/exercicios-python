import random

def random_num_creator(total_of_random_num):
   random_num_list = []

   while len(random_num_list) < total_of_random_num:
      random_num_list.append(random.randrange(0, 101, 2) )

   return random_num_list

total_of_random_num = int(input())
print(random_num_creator(total_of_random_num))