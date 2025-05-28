print("\t \t \t Name: Jay Surya \n\t \t \t USN: 1AY24AI048 \n\t \t \t Sec: M")

import random

streaks = 0

for trial in range(10000):  # Run the experiment 10,000 times
    flips = []
    for i in range(100):  # Flip the coin 100 times
        flips.append(random.choice(['H', 'T']))

    count = 1
    found_streak = False

    for i in range(1, 100):
        if flips[i] == flips[i - 1]:
            count += 1
            if count == 10:
                found_streak = True
                break
        else:
            count = 1

    if found_streak:
        streaks += 1

print("Streaks found:", streaks)
print("Chance of streak: {:.2f}%".format((streaks / 10000) * 100))
