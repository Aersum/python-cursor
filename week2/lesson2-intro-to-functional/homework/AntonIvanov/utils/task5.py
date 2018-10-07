def get_min_max_sum_age(memb: list):
    min_age = min(memb, key=lambda x: x['age'])
    max_age = max(memb, key=lambda x: x['age'])
    ages_list = [x['age'] for x in memb]
    sum_age = sum(ages_list)
    return sum_age, max_age, min_age
