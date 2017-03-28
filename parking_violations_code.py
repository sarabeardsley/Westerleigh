import csv
tickets = {}
f = open("Parking_Violations_Issued_Fiscal_Year_2016.csv")
reader = csv.DictReader(f)
for row in reader:
    plate = row["Plate ID"]
    tickets[plate] = tickets.get(plate,0) + 1

worst_plate = sorted(tickets, key = tickets.__getitem__, reverse=True)
for i in range(11):
    print("Plate ID", worst_plate[i], "has", tickets[worst_plate[i]], "tickets.")
