def cal_average(*grades):
    total_grades = len(grades)
    result = 0
    for grade in grades:
        result += grade
    return result / total_grades

print(cal_average(85, 90, 78, 92))
print(cal_average(100, 95))