import csv
with open('user_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in csvfile:
        data.append(row)

    print(data[1])
        