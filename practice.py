# def bitsChecker(bits):
#     count0 = 0
#     count1 = 0
#     l0 = []
#     l1 = []
#     f0 = 0
#     f1 = 1

#     for i in bits:
#         if i == '0':
#             count0 += 1
#         else:
#             l0.append(count0)
#             count0 = 0
    
#     for i in bits:
#         if i == '1':
#             count1 += 1

#         else:
#             l1.append(count1)
#             count1 = 0

#     l1.append(count1)
#     l0.append(count0)

#     for i in l0:
#         if i>0 and i%2 != 0:
#             f0 = 1
#             break
#     for i in l1:
#         if i > 0 and i%2 == 0:
#             f1 = 0
#             break
    
#     if f0 == 0 and f1 == 1:
#         return "Yes"
#     else:
#         return "No"

# print(bitsChecker('00111011'))


#problem2 solution
# data = input("Enter a String: ")
# data = list(data)
# vowels = ['a', 'e', 'i', 'o', 'u']

# op = ""

# temp = list(dict.fromkeys(data))
# print(temp)

# for i in temp:
#     if i in vowels:
#         c = data.count(i)
#         op = op + f"{c} {i} "
    
# print(op)
 
# def func(sentence):
#     first_letter = sentence[0]
#     words = sentence.split()
#     max_length = len( max(words,key=len))

#     # print(max_length_word)
#     new_words = []
#     for word in words:
#         if(len(word) < max_length):
#             new_words.append((int(max_length - len(word))* first_letter) + f'{word}')
#         else:
#             new_words.append(word)
#     print(new_words)
# func('this is a long string aaaaaaaaaa')

def func(str):
    newlist = ""
    ch = list(str)
    print(ch)
    for i in str:
        if i != " ":
            newlist = newlist + i
    
    print(newlist)






func('Your Task  is to Remove Space')