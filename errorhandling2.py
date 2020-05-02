
def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'somethig is wrong {err}')


print(sum(1, 0))
