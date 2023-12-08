from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class StudentNameChangerWindow(QDialog):
    def __init__(self, main_window):
        """
        Initialize the StudentNameChanger Window.

        Args:
        - main_window: Reference to the main GradeAssignerWindow.
        """
        super(StudentNameChangerWindow, self).__init__()

        # Initialize the StudentNameChanger Window
        self.setWindowTitle("Change Student Names")
        self.setGeometry(200, 200, 400, 300)

        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.instruction_label = QLabel("Please enter the names of the students you want:", self)
        self.layout.addWidget(self.instruction_label)

        self.name_labels = []
        self.name_inputs = []

        # Create input fields for student names
        for i in range(self.main_window.number_of_students):
            name_label = QLabel(f"Student {i + 1}:", self)
            name_input = QLineEdit(self)
            self.name_labels.append(name_label)
            self.name_inputs.append(name_input)

            self.layout.addWidget(name_label)
            self.layout.addWidget(name_input)

        self.save_button = QPushButton("SAVE", self)
        self.save_button.clicked.connect(self.save_changes)
        self.layout.addWidget(self.save_button)

        self.error_label = QLabel("", self)  # New label to display errors
        self.layout.addWidget(self.error_label)

        self.setLayout(self.layout)

    def save_changes(self):
        """
        Save changes based on entered names.
        """
        new_students = {}  # Use a temporary dictionary to avoid modification during iteration

        for i, input_field in enumerate(self.name_inputs):
            student_name = input_field.text().strip()

            # Validate student name
            if not student_name:
                self.error_label.setText("All students must be named.")
                return

            if any(char.isdigit() for char in student_name):
                self.error_label.setText("Only letters must be entered in the students' names.")
                return

            # Save the student names in the temporary dictionary
            new_students[student_name] = 0  # Set initial score to 0

        # Update the main window with the new student names
        self.main_window.students = new_students

        self.error_label.clear()  # Clear any previous error message
        self.accept()  # Close the dialog and return QDialog.Accepted
