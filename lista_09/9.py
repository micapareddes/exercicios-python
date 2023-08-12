def total_of_correct_answers(student_answer):
    ind = 0
    correct_answer = [ 'A', 'A', 'C', 'E', 'D', 'B', 'C', 'E', 'B', 'D' ]
    len_stud_ans = len(student_answer)
    len_cor_ans = len(correct_answer)
    counter_correct_answers = 0

    if len_stud_ans == len_cor_ans:
        while ind < len_stud_ans:
            current_stud_ans = student_answer[ind]
            current_cor_ans = correct_answer[ind]

            if (current_stud_ans != 'A' and current_stud_ans != 'B' and 
            current_stud_ans != 'C' and current_stud_ans != 'D' and
            current_stud_ans != 'E'):
                return 'Error: Apenas são permitidas as letras: A, B, C, D ou E.'

            if current_cor_ans == current_stud_ans:
                counter_correct_answers += 1
            ind += 1
            
        return counter_correct_answers
    return 'Error: A lista informada deve possuir 10 elementos.'

print(total_of_correct_answers(['A', 'A', 'B', 'B', 'B', 'D', 'B', 'B', 'B', 'D']))