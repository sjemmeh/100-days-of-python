# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
#
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 5]
#
# print(f"Short names: {short_names}")
# print(f"Long names: {long_names}")

# student_scores = {
#     "Alex": 80,
#     "Joe": 23,
#     "Sarah": 65,
#     "Beth": 56
# }
# passed_students = {name:score for (name,score) in student_scores.items() if score >= 60}
# print(passed_students)

import pandas

student_dict = {
    "Student": ["Angela", "James", "Lily"],
    "Score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.Student == "Angela":
        print(row.Score)