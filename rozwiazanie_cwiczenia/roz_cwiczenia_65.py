number_list = [1, -5, 3, -9, 25, 10, -99, 0, 25, 0]

# przykład 1
new_number_list_1 = sorted(number_list)
new_number_list_2 = sorted(number_list, reverse=True)
new_number_list = new_number_list_1 + new_number_list_2
print(new_number_list)


# # przykład 2
# new_number_list_1 = sorted(number_list)
# new_number_list_2 = sorted(number_list, reverse=True)
# new_number_list = new_number_list_1 + new_number_list_2
#
# for i in new_number_list:
#     print(i, end=' ')