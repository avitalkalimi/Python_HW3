# ******** HW3 ******** #
## part A Warm-up

def sudoku_is_legal(board):
    for i in range(len(board)):  # checking if the sudoku is legal
        cheking_list = []
        for j in range(len(board[i])):
            if board[i][j] not in cheking_list:
                cheking_list.append(board[i][j])
            else:
                return False

    cheking_list = []
    j = 0
    i = 0
    count = 0
    while count < 9:
        if board[i][j] not in cheking_list:
            cheking_list.append(board[i][j])
            i += 1
            if len(cheking_list) == 9:
                cheking_list = []
                j += 1
                i = 0
                count += 1
        else:
            return False

    cheking_list = []
    j = 0
    i = 0
    count = 0
    in_count = 0
    while count < 10:
        if count == 9:
            return True
        if in_count == 3:
            i += 3
            j = 0
            in_count = 0
        if board[i][j] not in cheking_list:
            cheking_list.append(board[i][j])
            if len(cheking_list) == 9:
                j += 1
                i = 0
                count += 1
                in_count += 1
                cheking_list = []
            elif len(cheking_list) % 3 == 0:
                i += 1
                j -= 2
            else:
                j += 1
        else:
            return False



## part B string manipulation
# function 1 change_tone
def change_tone(phrase, new_tone):  # change the tone of sentence
    if new_tone is True:
        if phrase.endswith("!?") is True:
            new_phrase = phrase.replace("!?", "")
            return new_phrase
        elif phrase.endswith("!") is True:
            new_phrase = phrase.replace("!", "?")
            return new_phrase
        elif phrase.endswith("?") is True:
            new_phrase = phrase.replace("?", "!")
            return new_phrase
        else:
            new_phrase = phrase + "!?"
            return new_phrase

    if new_tone is False:
        if phrase.endswith("!?") is True:
            new_phrase = phrase.replace("!?", "!")
            return new_phrase
        elif phrase.endswith("!") is True:
            new_phrase = phrase.replace("!", "!?")
            return new_phrase
        elif phrase.endswith("?") is True:
            new_phrase = phrase.replace("?", "")
            return new_phrase
        else:
            new_phrase = phrase + "?"
            return new_phrase

# function 2 be_polite
def be_polite(paragraph): # change the tone of paragraph
    splited_paragraph = paragraph.split(".")
    new_paragraph = ""
    for i in splited_paragraph:
        new_paragraph += change_tone(i, True) + "."
    if not paragraph[-1] == ".":
        return new_paragraph[:-1]
    return new_paragraph[:-1]

## part C data structures


# function 1 print_chars(phrase, reapeat)
def print_chars(phrase, repeat): # check order of chars
    first_list = list(phrase)
    if not repeat:
        the_set = set(first_list)
        secend_list = list(the_set)
        secend_list.sort()
        return secend_list
    first_list.sort()
    return first_list

# function a1 - orientation_day_registery
def orientation_day_registery(all_listed_students): # check registery of students
    students = {}
    for student in all_listed_students:
        firstname, lastname, grade = student.split(' ')
        grade = float(grade)
        grade = int(grade)
        if grade < 200 or grade > 800:
            grade = 200
        upper_firstname = firstname.upper()
        lower_firstname = firstname.lower()
        firstname = upper_firstname[0] + lower_firstname[1:]
        upper_lastname = lastname.upper()
        lower_lastname = lastname.lower()
        lastname = upper_lastname[0] + lower_lastname[1:]

        students[firstname + " " + lastname] = grade

    return students



# function b1 - get_number_of_honorary
def get_number_of_honors(students): # check how many students pass the tast
    count = 0
    for key in students.keys():
        if students[key] >= 750:
            count += 1
    return count



# function b2 - get_with_honors
def get_honors(students, min_grade): # getting names of students that pass the tast
    new_dict = {}
    for key, value in students.items():
        if value >= min_grade:
            new_dict[key] = value
    result = sorted(new_dict.items(), key=lambda kv: kv[1], reverse=True)

    names = []
    for i in result:
        names.append(i[0])
    return names


# function b3 - get_with_honors_by_avg
def get_with_honors_by_avg(students_list): # getting names of students that pass the tast and the average
    students = {}
    for student in students_list:
        firstname, lastname, grade = student.split(' ')
        grade = float(grade)
        grade = int(grade)
        if grade < 200 or grade > 800:
            grade = 200
        upper_firstname = firstname.upper()
        lower_firstname = firstname.lower()
        firstname = upper_firstname[0] + lower_firstname[1:]
        upper_lastname = lastname.upper()
        lower_lastname = lastname.lower()
        lastname = upper_lastname[0] + lower_lastname[1:]

        students[firstname + " " + lastname] = grade
    result = sorted(students.items(), key=lambda kv: kv[1], reverse=True)

    grade = []
    for i in result:
        grade.append(i[-1])
    sum_grade = sum(grade)
    count = len(grade)
    avg_grade = sum_grade / count

    names = []
    for i in result:
        if i[-1] >= avg_grade:
            names.append(i[0])


    return (avg_grade, names)

# ******** GOOD LUCK ******** #



