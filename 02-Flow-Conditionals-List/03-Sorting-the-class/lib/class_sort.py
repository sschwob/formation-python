def class_sort(students):
  # TODO: return (not print!) a copy of students, sorted alphabetically
  sorted_students = sorted(students, key = str.lower)
  return sorted_students
