from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from typing import Dict


class GradeComparerWindow(QDialog):
    def __init__(self, main_window):
        super(GradeComparerWindow, self).__init__()

        self.setWindowTitle("Grade Comparer")
        self.setGeometry(200, 200, 400, 300)

        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.instruction_label = QLabel("Please assign the grades the students got.", self)
        self.layout.addWidget(self.instruction_label)

        self.grade_inputs = []
        for student_name in self.main_window.students:
            label = QLabel(f"{student_name}:", self)
            grade_input = QLineEdit(self)
            grade_input.setPlaceholderText("Enter grade")
            percent_label = QLabel("%", self)

            self.grade_inputs.append(grade_input)
            self.layout.addWidget(label)
            self.layout.addWidget(grade_input)
            self.layout.addWidget(percent_label)

        self.compare_button = QPushButton("Compare Grades", self)
        self.compare_button.clicked.connect(self.compare_grades)
        self.layout.addWidget(self.compare_button)

        self.best_grade_label = QLabel("", self)
        self.worst_grade_label = QLabel("", self)
        self.duplicate_grade_label = QLabel("", self)
        self.layout.addWidget(self.best_grade_label)
        self.layout.addWidget(self.worst_grade_label)
        self.layout.addWidget(self.duplicate_grade_label)

        self.setLayout(self.layout)

    def compare_grades(self):
        grades = [float(grade_input.text().strip() or 0) for grade_input in self.grade_inputs]

        if any(grade < 0 or grade > 100 for grade in grades):
            self.best_grade_label.setText("Please enter grades between 0 and 100.")
            self.worst_grade_label.setText("")
            self.duplicate_grade_label.setText("")
            return

        if not all(grades):
            self.best_grade_label.setText("Please enter grades for all students.")
            self.worst_grade_label.setText("")
            self.duplicate_grade_label.setText("")
            return

        # Check for duplicate grades
        grade_count = {}
        duplicate_messages = []

        for student, grade in zip(self.main_window.students.keys(), grades):
            if grade in grade_count:
                grade_count[grade].append(student)
            else:
                grade_count[grade] = [student]

        # Filter out grades with only one student
        duplicate_grades = {grade: students for grade, students in grade_count.items() if len(students) > 1}

        # Display the duplicate grades message only if there are duplicates
        for grade, students in duplicate_grades.items():
            if len(students) == 2:
                duplicate_messages.append(f"{students[0]} and {students[1]} have the same grade: {grade}%")
            else:
                duplicate_messages.append(
                    f"{', '.join(students[:-1])}, and {students[-1]} have the same grade: {grade}%")

        # Update duplicate grade label accordingly
        if duplicate_messages:
            self.duplicate_grade_label.setText("\n".join(duplicate_messages))
        else:
            self.duplicate_grade_label.setText("")

        # Update labels for best and worst grades
        highest_index = grades.index(max(grades))
        lowest_index = grades.index(min(grades))

        best_student = list(self.main_window.students.keys())[highest_index]
        worst_student = list(self.main_window.students.keys())[lowest_index]

        self.best_grade_label.setText(f"{best_student} has the best grade: {max(grades)}%")
        self.worst_grade_label.setText(f"{worst_student} has the worst grade: {min(grades)}%")
