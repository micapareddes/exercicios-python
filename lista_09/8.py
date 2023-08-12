from statistics import mean
from statistics import mode

def median_and_mode_of_grades(grades_list):
    ind = 0
    len_list = len(grades_list)
    while ind < len_list:
        grade = grades_list[ind]
        if grade < 0 or grade > 10:
            return None
        ind += 1

    moda = mode(grades_list)
    media = mean(grades_list)

    return [media, moda]
print(median_and_mode_of_grades([1, 2, 3, 4]))
