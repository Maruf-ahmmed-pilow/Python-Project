questions = ("What science fiction novel by American writer ? : ",
             "How many elements are in the periodic table ? : ",
             "What is the symbol of Oxygen ? : ",
             "Which cricket team has most world-cup in history ? : ",
             "Which planet in the solar system is the hottest ? : ",
             )
options = (("A. George Lucas ", "B. TIE Fighters", "C. Electric Sheep", "D. Patrick Stewart"),
           ("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. O", "B. O2", "C. 2O2", "D. 3O2"),
           ("A. INDIA", "B. PAKISTAN", "C. ENGLAND", "D. AUSTRALIA"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
answer = ("C", "C", "A", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score +=1
        print("CORRECT!")

    else:
        print("INCORRECT!")
        print(f"{answer[question_num]} is the correct answer ")
    question_num +=1


print("----------------------------------------------")
print("                    RESULT                    ")
print("----------------------------------------------")

print(f"Your score is : {score} ", end=" ")

if score >= 3:
    print('CONGRATULATIONS! You are talented')

else:
    print("SHAME!, YOU NEED STUDY MORE")

print("Correct answer is : ", end=" ")
for ans in answer:
    print(ans, end = " ")
print()

print('You guesses : ', end=" ")
for guess in guesses:
    print(guess, end= " ")
