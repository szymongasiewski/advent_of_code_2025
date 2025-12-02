
id_ranges = None

with open("input.txt", "r", encoding="utf-8") as file:
    id_ranges = file.readlines()[0].split(",")

id_ranges = [list(map(int, (ids.split("-")))) for ids in id_ranges]

invalid_ids = []

for id_range in id_ranges:
    for id in range(id_range[0], id_range[1] + 1):
        str_id = str(id)

        for i in range(2, len(str_id) + 1):
            if str_id.count(str_id[:len(str_id)//i]) == i and len(str_id) % i == 0:
                invalid_ids.append(id)
                break

       
print(invalid_ids)
print(sum(invalid_ids))