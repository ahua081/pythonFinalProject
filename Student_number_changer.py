from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton
from logic import GradeAssignerLogic

class StudentNumberChangerWindow(QDialog):
    def __init__(self, main_window):
        """
        Initialize the StudentNumberChanger Window.

        Args:
        - main_window: Reference to the main GradeAssignerWindow.
        """
        super(StudentNumberChangerWindow, self).__init__()

        self.setWindowTitle("Change Number of Students")
        self.setGeometry(200, 200, 300, 200)

        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.instruction_label = QLabel("Please enter the number of students you want:", self)
        self.layout.addWidget(self.instruction_label)

        self.student_spin_box = QSpinBox(self)
        self.layout.addWidget(self.student_spin_box)

        self.error_label = QLabel("", self)  # New label to display errors
        self.layout.addWidget(self.error_label)

        self.save_button = QPushButton("SAVE", self)
        self.save_button.clicked.connect(self.save_changes)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def save_changes(self):
        """
        Save changes based on entered number of students.
        """
        new_student_count = self.student_spin_box.value()

        if new_student_count <= 1:
            self.error_label.setText("At least 2 students are required.")
            return

        # Update the main window with the new student count
        self.main_window.number_of_students = int(new_student_count)

        self.error_label.clear()  # Clear any previous error message
        self.accept()  # Close the dialog and return QDialog.Accepted
