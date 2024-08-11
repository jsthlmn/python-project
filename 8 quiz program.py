quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Milan"
    },
    "question4": {
        "question": "What is the capital of Sapin?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    }
}

score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score +1
        print("Your Score is: " + str(score))
    else:
        print("Wrong")
        print("The answer is : " + value['answer'])
        print("Your Score is : " + str(score))
        print("")
        print("")

print("You got" + str(score) + "out of 7 questions correctly")
print("Your percentage is" + str(int(score / 7  * 100)) + "%")