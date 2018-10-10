import os

def get_tree(path_dir: str, marker='|__'):
    # print(marker + os.listdir(path_dir)[0]
    cur_list = os.listdir(path_dir)
    if cur_list:
        for el in cur_list:
            if os.path.isfile(path_dir + '/' + el):
                print(len(marker) * ' ' + el)
            else:
                print(marker + el)
                get_tree(path_dir + '/' + el, 3*' '+marker)