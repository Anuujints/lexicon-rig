class Chat():
    """
    Welcomes user
    -------------
    Asks user to choose the difficulty of 
    the quiz he/she would like to take
    
    ------------
    User should only enter the number of the two choices
    """
    def __init__(self, message):
        self.message = message

    def lets_chat():
        chat = True
        while chat:
            start = ("Welcome to Lexicon-Rig Quiz World\n\n" +
                     "Let's get to know you a little bit we before start\n")
            name = input(start + "What is your name? ")
           
            answer = input(f"Hello, {name}! I hope your day has been going great." +
                            "\n\nPlease, choose your level of difficulty for the quiz." + ("\n(1) Hard\n(2) Easy\n\n"))
        
            if answer == "1":
                print("\n\nPlease, run (copy and paste) the following code in a new cell.\n\nQuestion.run_test(science)")
                chat = False
            elif answer == "2":
                print("\n\nPlease, run following code in a new cell.\n\nQuestion.run_test(history)")
                chat = False
            else:
                print("""\n\nIf you think you have clicked something accidentally, try running the program one more time. 
            \nIf not, thank you for taking your time and I wish you goodluck! Happy Studying!""")
                chat = False
                
class Question():
    def __init__(self, prompt, answer):
        """
        Parameters:
        ----------
        prompt: string
        answer: string
        
        Runs test:
        ----------
        Asks user's name and presents questions from the prompt
        Increments user's score based on their correct response
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

            
  
