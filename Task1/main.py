def total_salary(path: str) -> tuple:
    try:
        total_salary = 0
        developer_number = 0
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                salary = float(parts[1])
                total_salary += salary
                developer_number += 1
        averange_salary = total_salary / developer_number
        return f"Total salary: {total_salary}, average salary: {averange_salary}" 
    except Exception as e:
        print(f"The following error occured: {e}")
    except FileNotFoundError:
        print("File not found!")

path = "C:\!!!!!!GoIt Projects\goit-pycore-hw-04\goit-pycore-hw-04\Task1\salary.txt"

result = total_salary(path)

print(result)