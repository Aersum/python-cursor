from functools import reduce

def get_min_max_sum_age(memb: list):
    min_age = min(memb, key=lambda x: list(x.values())[0])
    max_age = max(memb, key=lambda x: list(x.values())[0])
    ages_list = [x['age'] for x in memb]
    sum_age = reduce(lambda x, y: x+y, ages_list)
    return tuple([sum_age, max_age, min_age])