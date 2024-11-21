score = float(input("Score: "))


if score == 100:
    print( "Score=", score , "Grade:A*")

elif score>= 90 and score <=99:
    print("Grade:A")
elif score>=80 and score <= 89:
    print("Grade:B")
elif score>=70 and score <= 79:
    print("Grade:C")
elif score>=60 and score <= 69:
    print("Grade:D")
elif score>=50 and score <= 59:
    print("Grade:E")
else:
    print ("Grade:F")
    print ("You Failed! Please Retake The Exam")

if score >= 60 and score<=100:
    print("Congrats You Passed!")




