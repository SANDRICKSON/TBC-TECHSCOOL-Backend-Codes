score = 10
question_list=[
    ("How much is 5+5 ", "10"),
    ("How much is 2+7 ", "9"),
    ("When was python created? ", "1991"),
    ("Which one is older Python or Java? ","python"),
    ("Which is capital of Georgia? ","Tbilisi")
]
index = 0
while index < len(question_list):
    answer = input(question_list[index][0])
    if answer == question_list[index][1]:
        index+=1
        score+=1
        print("correct")
    else:
        score -=1
print(f"Your score is {score}")