import random

class FruitQuiz:

    # Create a constructor
    def __init__(self):

        # Create a dictionary of fruits as keys and colour as value
        self.fruit={'apple':'red',
                    'orange':'orange',
                    'watermelon':'green',
                    'banana':'yellow'}

    def quiz(self):
        while(True):
            fruit,color = random.choice(list(self.fruit.items()))

            print("What is the colour of {}".format(fruit))
            user_answer = input()

            if(user_answer.lower() == color):
                print("Correct Answer")
            else:
                print("Wrong Answer")

            option = int(input("Enter 0, if you to play again otherwise enter 1 :"))

            if(option):
                break

print("Welcome to fruit quize")
fq = FruitQuiz()
fq.quiz()