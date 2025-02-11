import random


def get_valid_input():
    while True:
        try:
            number_of_students = int(input('How many students --> '))
            if number_of_students <= 0:
                print('Sorry, no numbers below zero\n')
            else:
                return number_of_students
        except ValueError:
            print('Invalid input. Only integers.\nTry again\n')


def create_students_dictionary(number_of_students):
    students = {}
    for i in range(number_of_students):
        score = random.randint(50, 100)
        verdict = random.choice(['Passed', 'Failed'])
        students[f'Student {i+1}'] = (score, verdict)
    return students


def find_passing_score(students):
    max_failing_score = 50
    min_passing_score = 100
    for score, verdict in students.values():
        if verdict == 'Failed' and score > max_failing_score:
            max_failing_score = score
        elif verdict == 'Passed' and score < min_passing_score:
            min_passing_score = score
    return max_failing_score, min_passing_score


def is_professor_consistent(max_failing_score, min_passing_score):
    if max_failing_score >= min_passing_score:
        print('The professor was not consistent.')
    else:
        print('The professor was consistent.')
        print(f'Range of passing scores: {max_failing_score} - {min_passing_score}')


def main():
    number_of_students = get_valid_input()
    students_dict = create_students_dictionary(number_of_students)
    failed_score, passed_score = find_passing_score(students_dict)
    is_professor_consistent(failed_score, passed_score)


main()
