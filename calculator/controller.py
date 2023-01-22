import view
import sum
import subtraction
import multiplication
import division
import division_int
import division_remainder


def calc():
    num_type = int(view.get_value(1))
    value_a = view.get_value(num_type)
    value_sign = view.get_sign()
    value_b= view.get_value(num_type)
    if value_sign == '+':
        result = sum.do_it(value_a, value_b)
    if value_sign == '-':
        result = subtraction.do_it(value_a, value_b)
    if value_sign == '*':
        result = multiplication.do_it(value_a, value_b)
    if value_sign == '/':
        result = division.do_it(value_a, value_b)

    if num_type == 1:
        if value_sign == '//':
            result = division_int.do_it(value_a, value_b)
        if value_sign == '%':
            result = division_remainder.do_it(value_a, value_b)
    if num_type != 1 and (value_sign == '//' or value_sign == '%'):
        print(f'Mistake. The sign {value_sign} cannot be used for complex numbers')
        exit()
 
    view.view_data(result)