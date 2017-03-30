# Westerleigh



Biggest 311 complaints:
 * Complaint Type Street Condition has 15489 complaints
 * Complaint Type Street Light Condition has 7856 complaints
 * Complaint Type Water System has 7247 complaints
 * Complaint Type Illegal Parking has 5359 complaints
 * Complaint Type Missed Collection (All Materials) has 4883 complaints
 * Complaint Type Sewer has 4716 complaints
 * Complaint Type Damaged Tree has 4698 complaints
 * Complaint Type Noise - Residential has 4028 complaints
 * Complaint Type Blocked Driveway has 3404 complaints
 * Complaint Type Sanitation Condition has 2949 complaints

License plates with the most tickets
* Plate ID BLANKPLATE has 74 tickets.
* Plate ID 152758A has 35 tickets.
* Plate ID 1995585 has 28 tickets.
* Plate ID 620545 has 22 tickets.
* Plate ID 77477JZ has 21 tickets.
* Plate ID HCU3682 has 20 tickets.
* Plate ID GWR3147 has 19 tickets.
* Plate ID HCL4140 has 19 tickets.
* Plate ID 1995584 has 18 tickets.
* Plate ID AG24908 has 18 tickets.
* Plate ID GYF1158 has 16 tickets.


311 code
* import csv
* numbercomplaints = {}
* f = open("311data10314.csv", encoding = 'utf-8')
* reader = csv.DictReader(f)
* for row in reader:
    complaint = row["Complaint Type"]
    numbercomplaints[complaint] = numbercomplaints.get(complaint, 0) + 1

* worst_complaint = sorted(numbercomplaints, key = numbercomplaints.__getitem__, reverse=True)
* for i in range(10):
    print("Complaint Type", worst_complaint[i], "has", numbercomplaints[worst_complaint[i]], "complaints")
    
 Westerleigh map code
* import csv
* tickets = {}
* f = open("Parking_Violations_Issued_Fiscal_Year_2016.csv")
* reader = csv.DictReader(f)
* for row in reader:
    plate = row["Plate ID"]
    tickets[plate] = tickets.get(plate,0) + 1

* worst_plate = sorted(tickets, key = tickets.__getitem__, reverse=True)
* for i in range(11):
    print("Plate ID", worst_plate[i], "has", tickets[worst_plate[i]], "tickets.")
