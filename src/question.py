           
class Question():
    def __init__(self, prompt, answer):
        """
        Parameters:
        ----------
        prompt: string
        answer: string
        
        ----------
        Asks user's name and presents questions from the prompts
        ----------
       
        Runs test:
            loops through prompts in questions
            if conditionals:
                   if the answer is correct
                       it increments score by 1      
        """
        self.prompt = prompt
        self.answer = answer
    
    def run_test(questions):
        name = input("Can you remind me your name again? ")
        score = 0
        
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
            print(f'\n\n{name}, you got ' + str(score) + '/' + str(len(questions)) + ' correct!')
           
        if score == len(questions):
            print("\n\nYay, you've got perfect score! You are good to go! ^^")
        else:
            print(f"\n\nIt's alright, {name}. You will get this next time. Let's practice more.")