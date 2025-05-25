score = 10
correct_count = 0
wrong_count = 0

question_list = [
    ("How much is 5+5? ", "10"),
    ("How much is 2+7? ", "9"),
    ("When was Python created? ", "1991"),
    ("Which one is older: Python or Java? ", "python"),
    ("What is the capital of Georgia? ", "Tbilisi")
]

index = 0

while index < len(question_list):
    question, correct_answer = question_list[index]
    user_answer = input(question).strip().lower()

    if user_answer == correct_answer.strip().lower():
        print("✅ Correct!")
        score += 1
        correct_count += 1
        index += 1
    else:
        print("❌ Wrong!")
        score -= 1
        wrong_count += 1

print("\n🎯 Quiz Completed!")
print(f"✅ Correct answers: {correct_count}")
print(f"❌ Wrong answers: {wrong_count}")
print(f"🏁 Final score: {score}")
