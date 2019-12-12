from question import Question
from prompts import science_prompts, history_prompts

class Chat():
    """
    Welcomes user
    -------------
    Asks user to choose the difficulty of 
    the quiz he/she would like to take
   
    ------------
    User should only enter the number of the two choices
    """
       
    def lets_chat(self):
        while 1:
            start = ("Welcome to Lexicon-Rig Quiz World\n\n" +
                     "Let's get to know you a little bit we before start\n")
            name = input(start + "What is your name? ")
           
            answer = input(f"Hello, {name}! I hope your day has been going great." \
                            "\n\nPlease, choose your level of difficulty for the quiz." \
                            "\n(1) Hard\n(2) Easy\n\n")
        
            if answer == "1":
                Question.run_test([
                    Question(science_prompts[0], "b"),
                    Question(science_prompts[1], "c"),
                    Question(science_prompts[2], "a"),
                    Question(science_prompts[3], "b"),
                    Question(science_prompts[4], "c"),
                    Question(science_prompts[5], "a"),
                    Question(science_prompts[6], "b"),
                    Question(science_prompts[7], "a"),
                    Question(science_prompts[8], "a"),
                    Question(science_prompts[9], "c")
                ])
                break
            elif answer == "2":
                Question.run_test([
                    Question(science_prompts[0], "b"),
                    Question(science_prompts[1], "c"),
                    Question(science_prompts[2], "a"),
                    Question(science_prompts[3], "b"),
                    Question(science_prompts[4], "c"),
                    Question(science_prompts[5], "a"),
                    Question(science_prompts[6], "b"),
                    Question(science_prompts[7], "a"),
                    Question(science_prompts[8], "a"),
                    Question(science_prompts[9], "c")
                ])
                break
            else:
                print("\n\nIf you think you have clicked something accidentally, " \
                    "try running the program one more time. \nIf not, thank you " \
                        "for taking your time and I wish you goodluck! Happy Studying!")
                break
     