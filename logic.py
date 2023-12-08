class GradeAssignerLogic:
    # Class to manage grade assigner logic

    @classmethod
    def compare_grades(cls, grades):
        best_student = max(grades)
        worst_student = min(grades)
        return f"{best_student} has the best grade: {max(grades)}%\n{worst_student} has the worst grade: {min(grades)}"
