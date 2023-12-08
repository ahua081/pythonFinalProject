from typing import Dict
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QDialog
from PyQt6.QtCore import Qt
from PyQt6 import uic
from Student_name_changer import StudentNameChangerWindow
from Student_number_changer import StudentNumberChangerWindow
from Grade_comparer import GradeComparerWindow

class GradeAssignerWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the GradeAssigner Window.

        Attributes:
        - central_widget: Main widget for the window.
        - layout: Vertical layout for the central widget.
        - title_label: TextEdit for the title.
        - message_label: TextEdit for the welcome message.
        - assign_button: Button to open GradeComparer window.
        - change_names_button: Button to open StudentNameChanger window.
        - change_number_button: Button to open StudentNumberChanger window.
        - exit_button: Button to exit the program.
        - students: Dictionary to store student names and grades.
        - number_of_students: Number of students to be graded.
        """
        super(GradeAssignerWindow, self).__init__()

        # Initialize the main window
        self.setWindowTitle("Grade Assigner")
        self.setGeometry(100, 100, 600, 400)

        # Set up the central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # Create and add widgets to the layout
        self.title_label = QTextEdit("Grade Assigner", self)
        self.title_label.setReadOnly(True)
        self.layout.addWidget(self.title_label)

        self.message_label = QTextEdit("Welcome to the Grade Assigner System. Please choose one of the buttons below.", self)
        self.message_label.setReadOnly(True)
        self.layout.addWidget(self.message_label)

        self.change_names_button = QPushButton("Change Names", self)
        self.change_number_button = QPushButton("Change Number of Students", self)
        self.assign_button = QPushButton("Assign Grades", self)
        self.exit_button = QPushButton("Exit", self)

        self.layout.addWidget(self.change_names_button)
        self.layout.addWidget(self.change_number_button)
        self.layout.addWidget(self.assign_button)
        self.layout.addWidget(self.exit_button)

        # Connect button clicks to corresponding methods
        self.change_names_button.clicked.connect(self.open_name_changer_window)
        self.change_number_button.clicked.connect(self.open_number_changer_window)
        self.assign_button.clicked.connect(self.open_grade_comparer_window)
        self.exit_button.clicked.connect(QApplication.instance().quit)

        # Set up the layout for the central widget
        self.central_widget.setLayout(self.layout)

        # Dictionary to store student names and grades
        self.students: Dict[str, int] = {}
        self.number_of_students: int = 0

    def open_name_changer_window(self):
        """
        Open the StudentNameChanger Window.
        ...
        """
        if not self.number_of_students:
            self.message_label.setPlainText("Please provide a number of students.")
            return

        name_changer_window = StudentNameChangerWindow(self)
        name_changer_window.exec()

    def open_number_changer_window(self):
        """
        Open the StudentNumberChanger Window.
        ...
        """
        number_changer_window = StudentNumberChangerWindow(self)
        number_changer_window.exec()

    def open_grade_comparer_window(self):
        """
        Open the GradeComparer Window.
        ...
        """
        if not self.number_of_students or len(self.students) != self.number_of_students:
            self.message_label.setPlainText("Please provide the number of students and enter their names.")
            return

        grade_comparer_window = GradeComparerWindow(self)
        grade_comparer_window.exec()

if __name__ == "__main__":
    app = QApplication([])
    main_window = GradeAssignerWindow()
    main_window.show()
    app.exec()
