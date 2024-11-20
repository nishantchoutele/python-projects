import time
import random

def multiplication_quiz():
    print("Welcome to multiplication quiz")
    print("You will be given 5 questions, answer as many as you can correctly!")
    print("Type exit if you want to exit the game")

    num_question = 5
    score = 0

    for i in range (1, num_question + 1):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)

        print(f"Question {i}: what is {num1} x {num2}? ")
        while True:
            user_input = input("Your answer:" ).strip()
            if user_input.lower() == 'exit':
                print("Exiting the Game, See you again!")
                return

            if user_input.isdigit():
                user_answer = int(user_input)
                break
            else:
                print(f"Invalid input, Please enter a number or type exit to exit the quiz.")

        correct_answer = num1* num2
        if user_answer == correct_answer:
            print ("Bravo you answer is Correct!")
            score +=1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
        print()
    print(f"Quiz Completed!")
    print(f"Your score: {score}/{num_question}")

    if score == num_question:
        print ("Execllent Work")
    elif score >= num_question//2:
        print(f"Good job! Keep practicing!")
    else:
        print(f"Don't give up, Keep Practicing.")

if __name__ == "__main__":
    multiplication_quiz()
        
        
        
                

                
