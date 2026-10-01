def student_details(name, roll_no):
    print("\n--- Student Details ---")
    print("Name:", name)
    print("Roll Number:", roll_no)


def calculate_total(m1, m2, m3):
    return m1 + m2 + m3


def calculate_average(total):
    return total / 3


def get_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"

def show_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"