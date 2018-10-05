def mkupper_name(memb: list):
    new_list = list(map(
        lambda x: {'age': x['age'], 'name': x['name'].upper()}, memb
        ))
    return new_list