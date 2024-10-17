
def get_cats_info(path: str) -> dict:
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line_parts = line.strip().split(",")
                id, name, age = line_parts
                age = int(age)
                cat_info = {
                    "id": id,
                    "name": name,
                    "age": age
                }
                cats.append(cat_info)
        return cats
    except FileNotFoundError:
        print("File not found!")

path = "C:\!!!!!!GoIt Projects\goit-pycore-hw-04\goit-pycore-hw-04\Task2\cats.txt"

cats_info = get_cats_info(path)

print(cats_info)