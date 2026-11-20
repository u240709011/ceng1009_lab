# my_list = [76,92,3,"hello",True,76,4]
# my_list.append("apple")
# my_list.append("76")
# my_list.insert(3,"cat")
# my_list.insert(0,99)
# print(my_list)
#
# print(my_list.index("hello"))
# print(my_list.count("76"))
# my_list.remove("76")
# print(my_list)
# my_list.pop(my_list.index(True))
# print(my_list)


# def sum_of_squares(number_list):
#     total = 0
#     for number in number_list:
#         total = total + number**2
#     return total
# my_list = [3, 4, 5,]
# print(sum_of_squares(my_list))

# def sum_evens(number_list):
#     total = 0
#     for number in number_list:
#         if number % 2 == 0:
#             total = total + number
#     return total
# my_list = [1,2,3, 4, 5,6,7,8,9,10]
# print(sum_evens(my_list))


# def count_five_letters(words):
#     count = 0
#     for letter in words:
#         if len(letter) == 5:
#             count += 1
#     return count
#
# my_list = ["apple","cat","lemon","python","tiger"]
# print(count_five_letters(my_list))


# def sum_elements_up_to_even(list):
#     sum = 0
#     for i in list:
#         if i % 2 == 0:
#             break
#         sum += i
#     return sum
#
# my_list = [1, 3,3,7, 5,6]
# print(sum_elements_up_to_even(my_list))

# def find_sam(list):
#     total = 1
#     for word in list:
#         if word=="sam":
#             break
#         else:
#             total += 1
#     return total
#
# my_list=[0,1,2,3,4,5,"sam",34]
# print(find_sam(my_list))


# def replace(s, old, new):
#     pieces = s.split(old)
#     return new.join(pieces)
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("WRONG")
# test(replace("Missisippi",'i','I'),"MIssIsIppI")

def max_value(list):
    maximum = list[0]
    for item in list:
        if item > maximum:
            maximum = item
    return maximum
my_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_value(my_list))