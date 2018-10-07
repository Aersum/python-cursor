import copy
from utils.task1 import members
from utils.task2 import mkupper_name
from utils.task3 import add_load
from utils.task4 import remain_member_o
from utils.task5 import get_min_max_sum_age
from utils.task6 import sort_by_namel_age
from utils.advanced import get_rome_number

if __name__ == "__main__":
    print("Task #1")
    print(members)

    print("Task #2")
    memb = copy.deepcopy(members)
    print(mkupper_name(memb))

    # print("Task #3")
    # print(add_load(members))
    #
    # print("Task #4")
    # print(remain_member_o(members))
    #
    # print("Task #5")
    # print(get_min_max_sum_age(members))
    #
    # print("Task #6")
    # print(sort_by_namel_age(members))
    #
    # print("Advanced Task")
    # print(get_rome_number(148))
    # print(get_rome_number(18))
    # print(get_rome_number(6))