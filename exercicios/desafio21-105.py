grade_info = {
    "Amount notes": 0,
    "Bigger note": 0,
    "Lower note": 0,
    "Average of class": 0
}


def grade():
    """
    Input and analyze notes.

        |line 17, global grade_info > sets the dictionary how global.
        |line 42-45, final def > adds and analyzes notes in the dictionary.
    :return: No return due dictionary set as global.
    """
    global grade_info
    amount_notes = str(input("How many notes do you input? "))
    if amount_notes.isnumeric() is True and amount_notes > "0":
        grade_class = []
        print(f"[Enter stop if do you want stop]")
        while True:
            amount_notes = int(amount_notes)
            for a in range(0, amount_notes):
                grade_stud = str(input("Enter a grade: "))
                if grade_stud.isalpha():
                    break
                grade_stud = float(grade_stud)
                grade_class.append(grade_stud)
            while True:
                stop = str(input("Do you add some more note [y/n]? ")).lower()
                if stop in "ny":
                    break
                else:
                    print("\033[31mThis isn't accept. try again!\033[m")
            if stop == "n":
                break
            else:
                amount_notes = str(input("How many notes do you input? "))
                print(f"[Enter stop if do you want stop]")

        grade_info["Amount notes"] = len(grade_class)
        grade_info["Bigger note"] = max(grade_class),
        grade_info["Lower note"] = min(grade_class),
        grade_info["Average of class"] = sum(grade_class) / len(grade_class)
    elif amount_notes.isalpha():
        grade()


def state(conf):
    """
    Analyze the situation of class.

    :param conf: Optional value, whether or not analyze the notes.
    :return: The situation, depending on the class average.
    """
    global average
    conf = input(conf)

    if conf is True:
        note_max = float(input("What do it the maximum note possible? "))
        note_min = float(input("What do it the minimum note possible? "))
        average_excellent = 80 / 100 * (note_max - note_min)
        average_good = 60 / 100 * (note_max - note_min)
        average_reasonable = 45 / 100 * (note_max - note_min)
        if average > average_excellent:
            return f"The situation of the class is EXCELLENT!"
        elif average > average_good:
            return f"The situation of the class is Good! "
        elif average > average_reasonable:
            return f"The situation of the class is Reasonable!"
        else:
            return f"The situation of the class is so Bad!"


grade()
print(f"{'Notes Information':-^30}")
for k, v in grade_info.items():
    print(f"-{k} is {v}.")
print('-' * 30)
average = grade_info["Average of class"]
print(state("You need see the situation of the class [y/n]? "))
print(f"{'End of the task':-^30}")
help(grade)
help(state)
#conf so amrcando true