def total_salary(path):

  total_salary = 0
  count = 0

  with open(path, 'r') as file:
    for line in file:
      name, salary = line.strip().split(',')
      total_salary += int(salary)
      count += 1

  average_salary = total_salary / count
  return total_salary, average_salary


file_path = "salaries.txt"
result = total_salary(file_path)
print("Загальна сума зарплат:", result[0])
print("Середня зарплата:", result[1])