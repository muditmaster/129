import csv

w = []
e = []

with open("bright_stars.csv","r") as t:
    csvreader = csv.reader(t)
    for row in csvreader:
        w.append(row)

with open("brown_dwarfs.csv","r") as t:
    csvreader = csv.reader(t)
    for row in csvreader:
        e.append(row)


headers_1 = w[0]
star_data_1 = w[1:]

headers_2 = e[0]
star_data_2 = e[1:]

headers = headers_1 + headers_2
star_data = []
for index, data_row in enumerate(star_data_1):
    star_data.append(star_data_1[index] + star_data_2[index])

with open("merged_dataset1.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

    

























