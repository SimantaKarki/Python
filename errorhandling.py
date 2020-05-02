# error handling

while True:
    try:
        age = int(input('what is your age?'))
        10/age
        raise Exception('hey cut it out')
    # except ValueError:
    #     print('Please enter a number')

    except ZeroDivisionError:
        print('Please enter a number greater than 0')

    else:
        print('thank you!')
        break
    finally:
        print('ok i am finally done')
