def get_cats_info(path):

  cats = []
  with open(path, 'r') as file:
    for line in file:
      cat_id, name, age = line.strip().split(',')
      cat = {'id': cat_id, 'name': name, 'age': int(age)}
      cats.append(cat)
  return cats


file_path = "cats.txt"
cats_data = get_cats_info(file_path)
print(cats_data)