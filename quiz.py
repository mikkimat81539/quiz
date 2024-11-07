"""Create a multiple-choice quiz with a set of questions stored in a list.
Use a loop to iterate through the questions, prompting the user for answers."""

# I need to create a list of questions
# I need to create the answers

questions = ["What is 2 + 2? ",
             "What is the capital of Texas? ",
             "How many fingers does a human have? "]

correct = ["4", "austin", "10"]

for i in range(len(questions)):
    answers = input(questions[i]).lower()

    if answers == correct[i]:
        print("Correct")
    else:
        print("Wrong")
