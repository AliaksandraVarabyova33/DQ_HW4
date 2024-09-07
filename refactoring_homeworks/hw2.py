from random import randint, choice
from string import ascii_lowercase

def create_random_list_of_dicts():
  return [{choice(ascii_lowercase): randint(0, 100) for i in range(5)} for j in range(randint(2, 10))]

def transform_to_dict_of_dicts(rand_list):
  tmp_dict = {}
  count = 0
  for dictionary in rand_list:
    count += 1
    for k, v in dictionary.items():
      tmp_dict.setdefault(k, {}).setdefault(v, count)
  return tmp_dict

def create_final_dict(tmp_dict):
  final_dict = {}
  for k, v in tmp_dict.items():
    if len(v) > 1:
     final_dict[k + "_"+str(v.get(max(v)))] = max(v)
    else: final_dict[k] = next(iter(v.keys()))
  return final_dict

rand_list = create_random_list_of_dicts()

print(rand_list)

print(create_final_dict(transform_to_dict_of_dicts(rand_list)))


