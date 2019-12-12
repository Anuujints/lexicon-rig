from Question import Question

q_prompts = [
    "What team Lebron Jameas play?\n(a) Lakers\n(b) Boston Celtics\n(c) Golden State Warriors\n\n",
    "Which continent is Germany located?\n(a) Asia\n(b) Africa\n(c) Europe\n\n"
]

questions = [
    Question(q_prompts[0], "a"),
    Question(q_prompts[1], "c")
]

#   def run_quiz(self):
#     score = 0
    
    
#     for item in :
#         answer = input(item.questions)
#         if answer == item.answers:
#             score +=1

def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct!')

run_test(questions)