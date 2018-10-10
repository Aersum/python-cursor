import csv


def create_csv(dict_list: list, file_name: str):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = list(dict_list[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in dict_list:
            writer.writerow(i)
    print(f'"{file_name}" created')
