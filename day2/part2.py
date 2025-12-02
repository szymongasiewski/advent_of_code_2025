
id_ranges = None

with open("input.txt", "r", encoding="utf-8") as file:
    id_ranges = file.readlines()[0].split(",")

id_ranges = [list(map(int, (ids.split("-")))) for ids in id_ranges]

invalid_ids = []

for id_range in id_ranges:
    for id in range(id_range[0], id_range[1] + 1):
        str_id = str(id)

        if str_id in (str_id + str_id)[1:-1]:
            invalid_ids.append(id)

       
print(invalid_ids)
print(sum(invalid_ids))