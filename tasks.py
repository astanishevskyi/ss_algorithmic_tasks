"""
python 3.7
author: Andrew Stanishevskyi
"""


def task_108(n):
    """
    Дано натуральное число n. Получить наименьшее число
    вида 2^r , превосходящее n.
    """
    try:
        input_value = int(n)
        if input_value > 0:
            for i in range(input_value + 1):
                two_to_i_power = 2 ** i
                if two_to_i_power > input_value:
                    return two_to_i_power
        else:
            return 'n must be bigger than 0'
    except ValueError:
        return 'Type integer'


def task_331_a(n):
    """
    Дано натуральное число n. Можно ли представить его в
    виде суммы трех квадратов натуральных чисел? Если можно,
    то указать тройку x, y, z таких натуральных чисел, что
    n = x^2 + y^2 + z^2
    """
    try:
        input_value = int(n)
        if input_value > 0:

            for x in range(input_value + 1):
                for y in range(input_value + 1):
                    for z in range(input_value + 1):
                        if x ** 2 + y ** 2 + z ** 2 == input_value:
                            return [x, y, z]

            return 'There is no x, y, z'

        else:
            return 'n must be bigger than 0'

    except ValueError:
        return 'Type integer'


def task_331_b(n):
    """
    Дано натуральное число n. Можно ли представить его в
    виде суммы трех квадратов натуральных чисел? Если можно, то
    указать все тройки x, y, z таких натуральных чисел, что
    n = x^2 + y^2 + z^2 .
    """

    try:
        input_value = int(n)

        if input_value > 0:

            output = []
            for x in range(input_value + 1):
                for y in range(input_value + 1):
                    for z in range(input_value + 1):
                        if x ** 2 + y ** 2 + z ** 2 == input_value:
                            output.append([x, y, z])

            return output
        else:
            return 'n must be bigger than 0'
    except ValueError:
        return 'Type integer'
