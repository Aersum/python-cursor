def add_load(memb: list):
    max_age = 200
    new_list = list(map(
        lambda x: {
            'age': x['age'],
            'name': x['name'],
            'load': x['age'] / max_age * 100
        }, memb))
    return new_list
