score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A, Well done!")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >=70 and score < 80:
    print("Grade: C")
else:
    print("You have a shit score, do some revision!")
