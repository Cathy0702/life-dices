import datetime
import random
import csv

counter = 11

target = "1" * counter
now = datetime.datetime.now()

check = ""
for i in range(counter):
    roll = random.randint(1, 6)
    check += str(roll)

with open("dice.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([now, check])

if check == target:
    with open("ELEPHANT", "w") as file:
        file.write(f"----------- {now} TADA! IT IS THE ELEPHANT!-----------\n")