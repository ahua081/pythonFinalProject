from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class GradeComparerWindow(QDialog):
    def __init__(self, main_window):
        """
        Initialize the GradeComparer Window.

        Args:
        - main_window: Reference to the main GradeAssignerWindow.
        """
        super(GradeComparerWindow, self).__init__()

        # Initialize the GradeComparer Window
        self.setWindowTitle("Grade Comparer")
        self.setGeometry(200, 200, 400, 300)

        self.main_window = main_window

        self.layout = QVBoxLayout()

        # Add a text box saying "Please assign the grades the students got."
        self.instruction_label = QLabel("Please assign the grades the students got.", self)
        self.layout.addWidget(self.instruction_label)

        # Add input boxes for each student to assign grades
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

        # Add Compare Grades button
        self.compare_button = QPushButton("Compare Grades", self)
        self.compare_button.clicked.connect(self.compare_grades)
        self.layout.addWidget(self.compare_button)

        # Add labels for best and worst grades
        self.best_grade_label = QLabel("", self)
        self.worst_grade_label = QLabel("", self)
        self.layout.addWidget(self.best_grade_label)
        self.layout.addWidget(self.worst_grade_label)

        self.setLayout(self.layout)

    def compare_grades(self):
        """
        Compare grades and update the labels with the best and worst grades.
        """
        grades = []

        try:
            for grade_input in self.grade_inputs:
                grade_text = grade_input.text().strip()

                # Check if the grade is not empty
                if not grade_text:
                    raise ValueError("Please enter grades for all students.")

                try:
                    # Attempt to convert the grade to a float
                    grade = float(grade_text)
                except ValueError:
                    raise ValueError("Please enter valid numerical grades.")

                # Check if the grade is between 0 and 100
                if not (0 <= grade <= 100):
                    raise ValueError("Please enter grades between 0 and 100.")

                grades.append(grade)

        except ValueError as e:
            # Display the specific error message
            self.best_grade_label.setText(f"Invalid Input: {e}")
            self.worst_grade_label.setText("")
            return

        # Check if there are any grades entered
        if not grades:
            self.best_grade_label.setText("No grades entered.")
            self.worst_grade_label.setText("")
            return

        # Find the student with the highest and lowest grades
        highest_index = grades.index(max(grades))
        lowest_index = grades.index(min(grades))

        # Update the labels with the best and worst grades
        best_student = list(self.main_window.students.keys())[highest_index]
        worst_student = list(self.main_window.students.keys())[lowest_index]

        self.best_grade_label.setText(f"{best_student} has the best grade: {max(grades)}%")
        self.worst_grade_label.setText(f"{worst_student} has the worst grade: {min(grades)}%")
