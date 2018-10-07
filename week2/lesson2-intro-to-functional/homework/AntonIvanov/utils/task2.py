def mkupper_name(memb: list):
    for i in memb:
        i['name'] = i['name'].upper()
    return memb
