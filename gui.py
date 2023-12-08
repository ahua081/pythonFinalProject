from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QTextEdit, QDialog
from PyQt6 import uic
from logic import GradeAssignerLogic
from student_name_changer import StudentNameChangerWindow
from student_number_changer import StudentNumberChangerWindow
from grade_comparer import GradeComparerWindow

class GradeAssignerWindow(QMainWindow):
    def __init__(self):
        super(GradeAssignerWindow, self).__init__()

        # Initialize the main window
        uic.loadUi('grade_assigner.ui', self)
        self.setWindowTitle("Grade Assigner")
        self.setGeometry(100, 100, 400, 300)

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
        self.assign_grades_button = QPushButton("Assign Grades", self)

        self.layout.addWidget(self.change_names_button)
        self.layout.addWidget(self.change_number_button)
        self.layout.addWidget(self.assign_grades_button)

        # Connect button clicks to corresponding methods
        self.change_names_button.clicked.connect(self.open_name_changer_window)
        self.change_number_button.clicked.connect(self.open_number_changer_window)
        self.assign_grades_button.clicked.connect(self.open_grade_comparer_window)

        # Set up the layout for the central widget
        self.central_widget.setLayout(self.layout)

    def open_name_changer_window(self):
        name_changer_window = StudentNameChangerWindow(self)
        name_changer_window.exec()

    def open_number_changer_window(self):
        number_changer_window = StudentNumberChangerWindow(self)
        number_changer_window.exec()

    def open_grade_comparer_window(self):
        comparer_window = GradeComparerWindow(self)
        comparer_window.exec()

if __name__ == "__main__":
    app = QApplication([])
    main_window = GradeAssignerWindow()
    main_window.show()
    app.exec()
