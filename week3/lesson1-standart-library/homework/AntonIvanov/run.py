from utils.task1 import get_tree
from utils.task2 import create_csv
from utils.userlist import user_list
import os

print("Task 1")
get_tree(os.getcwd() + "/utils/tree")
print("Task 2")
create_csv(user_list, 'userlist.csv')
