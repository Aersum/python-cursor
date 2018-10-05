def sort_by_namel_age(memb: list):
    return sorted(memb, key=lambda x: (len(x['name']), x['age']))
