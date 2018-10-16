from task1 import *


class ITcompany:
    dev_list = []

    def __add__(self, developer):
        self.dev_list.append(developer)
        if developer.years_experience < 3:
            print("Developer experience is not enough")
        # self.dev_list.sort(key=lambda developer: developer.years_experience)
        return self

    def __str__(self):
        sorted_list = sorted(self.dev_list, key=lambda developer: developer.years_experience)
        print_dev_list = [f"{i.name} - {i.years_experience} years, {i.language}" for i in sorted_list]
        return '\n'.join(print_dev_list)

    def fire(self, dev_name: str):
        if dev_name in [i.name for i in self.dev_list]:
            for i in self.dev_list:
                if i.name == dev_name:
                    self.dev_list.remove(i)
                    print(f"Developer with name {dev_name} fired")
                    break
        else:
            print(f"Developer with name {dev_name} not found in the list")
