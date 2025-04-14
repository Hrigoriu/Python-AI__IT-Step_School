def get_best_students(input_file, output_file='files\\output.txt'):
    students = list()

    with open(input_file, 'r') as read_file:
        students = [line.strip() for line in read_file if line.strip()]

    with open(output_file, 'w') as write_file:
        for student in students:
            student = student.split()
            if len(student) >= 3:
                name = student[0]
                rating = list(map(int, student[2:]))
                if sum(rating) / len(rating) > 6:
                    print(name, sep='\n', file=write_file)


get_best_students('files\\input.txt')