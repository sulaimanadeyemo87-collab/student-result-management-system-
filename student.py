from dataclasses import dataclass, asdict

@dataclass
class Student:
    student_id: str
    full_name: str
    class_form: str
    gender: str
    date_of_birth: str

    def to_dict(self):
        return {
            **asdict(self),
            "scores": {},
            "score_dates": {}
        }
