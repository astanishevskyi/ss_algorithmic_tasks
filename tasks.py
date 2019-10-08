"""
python 3.7
author: Andrew Stanishevskyi
"""


def task_108(input_data):
    """
    Дано натуральное число n. Получить наименьшее число
    вида 2^r , превосходящее n.
    """
    try:
        input_data = int(input_data)
        if input_data > 0:
            for i in range(input_data + 1):
                two_to_i_power = 2 ** i
                if two_to_i_power > input_data:
                    return two_to_i_power
        else:
            return 'n must be bigger than 0'
    except ValueError:
        return 'Type integer'


def task_331_a(input_data):
    """
    Дано натуральное число n. Можно ли представить его в
    виде суммы трех квадратов натуральных чисел? Если можно,
    то указать тройку x, y, z таких натуральных чисел, что
    n = x^2 + y^2 + z^2
    """
    try:
        input_data = int(input_data)
        if input_data > 0:

            for x_arg in range(input_data + 1):
                for y_arg in range(input_data + 1):
                    for z_arg in range(input_data + 1):
                        if x_arg ** 2 + y_arg ** 2 + z_arg ** 2 == input_data:
                            return [x_arg, y_arg, z_arg]

            return 'There is no x, y, z'

        else:
            return 'n must be bigger than 0'

    except ValueError:
        return 'Type integer'


def task_331_b(input_data):
    """
    Дано натуральное число n. Можно ли представить его в
    виде суммы трех квадратов натуральных чисел? Если можно, то
    указать все тройки x, y, z таких натуральных чисел, что
    n = x^2 + y^2 + z^2 .
    """

    try:
        input_data = int(input_data)

        if input_data > 0:

            output = []
            for x_arg in range(input_data + 1):
                for y_arg in range(input_data + 1):
                    for z_arg in range(input_data + 1):
                        if x_arg ** 2 + y_arg ** 2 + z_arg ** 2 == input_data:
                            output.append([x_arg, y_arg, z_arg])

            return output
        else:
            return 'n must be bigger than 0'
    except ValueError:
        return 'Type integer'
