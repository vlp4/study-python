import re


def parse_course_line(s: str) -> tuple:
    parts = s.split(':', 2)
    course_name = None
    classes = {}
    if len(parts) == 2:
        course_name = parts[0]
        classes_str = parts[1]
        pattern = re.compile('(\d+)\((\w+)\)')
        for class_item in pattern.finditer(classes_str):
            class_count = int(class_item.group(1))
            class_type = class_item.group(2)
            classes[class_type] = class_count

    return course_name, classes


courses = {}

# Load courses data
with open('data/task6-input.txt', 'r') as infile:
    for line in infile:
        name, classes = parse_course_line(line)
        if name:
            courses[name] = classes
print('Курсы:', courses)

# Calculate course totals
course_totals = {}
for name, classes in courses.items():
    course_totals[name] = sum(classes.values())

print('Суммарно количество занятий в курсах:', course_totals)
