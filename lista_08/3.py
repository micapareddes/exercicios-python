def verify_if_test_score_is_valid(test_score):
    return 0 <= test_score <= 10

test = verify_if_test_score_is_valid(-1)
print(test)


# O excercício mencionou que queria utilizar a função do exercício 1 ou 2 na sua nova função.
''''
def verify_if_test_score_is_valid(test_score):
    return verify_if_num_in_interval(0, 10, test_score)
'''