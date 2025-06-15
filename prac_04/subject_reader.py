FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subjects(subjects):
    """Display subject details in formatted output."""
    for subject in subjects:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")


main()
