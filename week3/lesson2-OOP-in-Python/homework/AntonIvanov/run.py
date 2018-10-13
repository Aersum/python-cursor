from utils.task1 import *

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
