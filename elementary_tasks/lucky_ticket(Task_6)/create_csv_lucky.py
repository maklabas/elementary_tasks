import csv

with open("lucky_tickets.csv", mode='w', encoding='utf-8') as db:
    # names = ['Moskow', 'Piter']
    names = ['Number']
    file_writer = csv.DictWriter(db, delimiter=',', lineterminator='\r', fieldnames=names)
    file_writer.writeheader()

    for i in range(300000, 800000):
        file_writer.writerow({"Number": i})
