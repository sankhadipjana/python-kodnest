
from abc import ABC, abstractmethod



class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)


    def get_matched_skills(self):
        return self.student_skills & self.required_skills


    # Add abstract analyze()



class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        matched = len(self.get_matched_skills())
        required = len(self.required_skills)
        return matched / required * 100


    # Implement analyze()



class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        return self.required_skills - self.student_skills


    # Implement analyze()



student_skills = input().split()
required_skills = input().split()


# Create both analyzers and print their analyze() results




