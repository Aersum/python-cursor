def remain_member_o(member_list: list):
    return list(filter(lambda x: 'o' in x['name'], member_list))
