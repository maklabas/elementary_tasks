import csv
marker = input("Enter marker: ")
with open("lucky_tickets.csv", mode='w', encoding='utf-8') as db:
    # names = ['Moskow', 'Piter']
    names = [marker]
    file_writer = csv.DictWriter(db, delimiter=',', lineterminator='\r', fieldnames=names)
    file_writer.writeheader()

    for i in range(300000, 800000):
        file_writer.writerow({marker: i})
