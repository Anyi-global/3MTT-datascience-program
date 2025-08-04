'''
1. Quiz Game
Task: Create a quiz game made up of 5 questions. The user should be able to enter in answers and the final score calculated.

Objective: To create a Python-based quiz game that allows users to answer 5 questions interactively and calculates their final score based on correct answers.

Acceptance Criteria:

The quiz contains exactly five questions.
Questions and answers are stored in an easily modifiable structure (e.g., a list of dictionaries).
The user can input their answers, and responses are case-insensitive.
Correct answers increase the score, and incorrect answers display the correct answer.
The final score is displayed at the end of the quiz.
'''

Questions = [
    {"question": "Who is the president of Nigeria?", "answer": "Tinubu"},
    {"question": "The temporary storage device in a computer is called?", "answer": "RAM"},
    {"question": "Raw or basic fact about an entity is called?", "answer": "Data"},
    {"question": "The organization of data in a program for easy access is called?", "answer": "Data Structure"},
    {"question": "What is the full name of our Data Science instructor at Darey.io?", "answer": "Hannah Igboke"}
]

total_score = 0

for ques in Questions:
    print(f'\n{ques["question"]}')
    Answer = input("Enter your answer: ").strip().lower()
    
    if Answer == ques["answer"].lower():
        point = 1
        total_score += 1
        print("\nCorrect Answer!", point, 'point')
    elif Answer == ques["answer"].lower():
        point = 1
        total_score += 1
        print("\nCorrect Answer!", point, 'point')
    elif Answer == ques["answer"].lower():
        point = 1
        total_score += 1
        print("\nCorrect Answer!", point, 'point')
    elif Answer == ques["answer"].lower():
        point = 1
        total_score += 1
        print("\nCorrect Answer!", point, 'point')
    elif Answer == ques["answer"].lower():
        point = 1
        total_score += 1
        print("\nCorrect Answer!", point, 'point')
    else:
        print(f"Wrong answer! The correct answer is: {ques["answer"]}")
print(f'\nTotal Points = {total_score}')

