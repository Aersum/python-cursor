from utils.task1 import *
from utils.task2 import *
from utils.task3 import *
import pprint

if __name__ == "__main__":
    print(5*'*' + "Task 1" + 5*'*')
    python_dev = PythonDeveloper("Anton", 2)
    python_dev.about()
    python_dev.write_code()
    print(python_dev)
    python_dev()

    print ("*"*5)
    java_dev = JavaDeveloper("Oleg", 7)
    java_dev.about()
    java_dev.write_code()
    print(java_dev)
    java_dev()

    print("*" * 5)
    ruby_dev = RubyDeveloper("Max", 4)
    ruby_dev.about()
    ruby_dev.write_code()
    print(ruby_dev)
    ruby_dev()

    print(5*'*' + "Task 2" + 5*'*')
    pprint.pprint(E.mro())

    print(5 * '*' + "Task 3" + 5 * '*')
    it_company = ITcompany()
    it_company += python_dev
    it_company += java_dev
    it_company += ruby_dev
    it_company += PythonDeveloper("Elena", 12)
    it_company += JavaDeveloper("Mickle", 1)
    print(it_company)
    it_company.fire("Anton")
    print(it_company)
    it_company.fire("Alex")
    print(it_company)
