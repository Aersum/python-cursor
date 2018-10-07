def add_load(memb: list):
    max_age = 200
    filt_list = list(filter(lambda x: x['age'] < max_age, memb))
    for i in filt_list:
        i['load'] = i['age'] / max_age * 100
    return filt_list
