# employees = [
#     {"employee_id": "E101", "name": "Asha", "department": "Development"}, 
#     {"employee_id": "E102", "name": "Ravi", "department": "Testing"}, 
#     {"employee_id": "E103", "name": "Meera", "department": "Support"}
# ]
# print(employees)
# employee_by_id = {}
# for employee in employees:
#     employee_id = employee["employee_id"]
#     employee_by_id[employee_id] = employee
# print(employee_by_id)    

import numbers
import numbers
import numbers
numbers = [11, 18, 23, 30, 42, 55]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


skills = ["Python", "SQL", "Java", "React", "C"]
long_skills = [skill for skill in skills if len (skill) >= 4]
print(long_skills)

names = ["Asha", "arun", "Meera", "mohan"]
capitalized_names = [name for name in names if name[0].isupper()]
print(capitalized_names)

products = [
["Keyboard", 8],
["Mouse", 0],
["Monitor", 5],
["Webcam", 3]
]
products_under_price5 = [product[0] for product in products if product[1] < 5]
print(products_under_price5)



numbers = [5, 12, 28, 55, 43, 8, 50]
selected_numbers = [
    number
    for number in numbers
    if number >= 10 and number <= 50 
    ]
print(selected_numbers)


number2 = [3, 8, 11, 16, 21]
even_number2 = [number for number in number2 if number % 2 == 0]
print(number2)
print(even_number2)


scores = [12, 23, 34, 54, 65, 13, 39, 56, 76, 86]
passing_scores = [score for score in scores if score >= 40]

def is_valid_score(score):
    return score >= 0 and score <= 100
valid_scores = [score for score in scores if is_valid_score(score)]
print(passing_scores)