"""
python 3.7
author: Andrew Stanishevskyi
"""

from tasks import task_108, task_331_a, task_331_b


def main():
    """
    Menu for all the tasks
    :return: None
    """
    while True:
        select_task = input('Enter task to execute (108/331a/331b): ')
        if select_task == '108':
            input_data = input()
            print(task_108(input_data))
        elif select_task == '331a':
            input_data = input()
            print(task_331_a(input_data))
        elif select_task == '331b':
            input_data = input()
            print(task_331_b(input_data))
        else:
            print('Type 108 or 331a or 331b')


if __name__ == '__main__':
    main()
