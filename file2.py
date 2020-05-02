try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.readlines())
except FileNotFoundError as err:
    print('file does not exist')
