import csv
numbercomplaints = {}
f = open("311data10314.csv", encoding = 'utf-8')
reader = csv.DictReader(f)
for row in reader:
    complaint = row["Complaint Type"]
    numbercomplaints[complaint] = numbercomplaints.get(complaint, 0) + 1

worst_complaint = sorted(numbercomplaints, key = numbercomplaints.__getitem__, reverse=True)
for i in range(10):
    print("Complaint Type", worst_complaint[i], "has", numbercomplaints[worst_complaint[i]], "complaints")


