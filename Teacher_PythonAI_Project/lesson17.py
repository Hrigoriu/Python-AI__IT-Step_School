
with open('files\\data.txt', 'r') as file:
    counter = 0

    for line in file:
        counter += 1

    print(counter)

    # print(len(file.readlines()))
