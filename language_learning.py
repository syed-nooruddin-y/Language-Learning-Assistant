import sys
import random
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
import os
import time

while True:
    print("WELCOME THERE")
    NAME = input("ENTER YOUR NAME: ")
    print("NICE NAME", NAME.upper().strip())
    time.sleep(3)
    print("Ok, let's learn something nice today")
    print("1. IRISH, 2. HAWAIIAN")
    choices = (1, 2)
    CHOICE = int(input("ENTER YOUR CHOICE: "))
    time.sleep(2)
    
    if CHOICE not in choices:
        print("There is no choice like that")
        sys.exit()

    if CHOICE == 1:
        phrases = """\n
                  Hello: Dia dhuit
                  Goodbye: Slán
                  Please: Le do thoil
                  Thank you: Go raibh maith agat
                  Yes: Tá
                  No: Níl
                  """
    elif CHOICE == 2:
        phrases = """\n
                  Hello: Aloha
                  Goodbye: Aloha
                  Please: ʻOluʻolu
                  Thank you: Mahalo
                  Yes: ʻAe
                  No: ʻAʻole
                  """
 

   time.sleep(2)
    print("HERE ARE SOME COMMON PHRASES:")
    print(phrases)
    print("DO YOU WANT TO SEE YOUR PROGRESS?")
    ANSWER1 = int(input("Choose 1 for YES and 2 for NO: "))
    if ANSWER1 == 1:
        x = np.linspace(1, 5, 6)
        y = np.log(x)
        plt.plot(x, y)
        plt.xlabel('Study Sessions')
        plt.ylabel('Progress')
        plt.title('Language Learning Progress')
        plt.show()
        print("\n\n{This is just a hypothetical graph}")
    else:
        print("Ok, let's talk about it later")
    time.sleep(2)    

    print("GOING AHEAD WITH SOME EXTRA WORDS")
    if CHOICE == 1:
        print("""
              Nice to meet you: deas bualadh leat
              Good Morning: maidin mhaith
              Good Evening: trathnona maith
              Good Night: oiche mhaith
              How is your day going: conas ata tu ag dul""")
    elif CHOICE == 2:
        print("""\n
              Nice to meet you: maika'i ka launa 'ana me 'oe
              Good Morning: Aloha kakahiaka
              Good Evening: Aloha ahiahi
              Good Night: Aloha po
              How is your day going: pehea kou la""")

    print("Let's see how many more words we could learn")
    NUMBER = random.randint(1, 5)
    print(NUMBER)
    time.sleep(2)

    if CHOICE == 1:
        if NUMBER == 1:
            print("cad is ainm duit-What is your name?")
        elif NUMBER == 2:
            print("cad is ainm duit-What is your name","\n Dia duit ar domhan-hello world")
        elif NUMBER == 3:
            print("maidin mhaith-good morning ","\nDia duit ar domhan-hello world","\ncad is ainm duit-What is your name?","\nmaidin mhaith-good morning ")
        elif NUMBER == 4:
            print("deas-nice","\nDia duit ar domhan-hello world","\ncad is ainm duit-What is your name?","\nmaidin mhaith-good morning ","\ndeas bualadh leat-nice meeting you")
        elif NUMBER == 5:
            print("an raibh do lon agat?-had your lunch","\nDia duit ar domhan-hello world","\ncad is ainm duit-What is your name?","\nmaidin mhaith-good morning ","\nan raibh do lon agat?-had your lunch")
      

  elif NUMBER == 6:
            print("deas bualadh leat-nice meeting you","\nDia duit ar domhan-hello world","\ncad is ainm duit-What is your name?","\nmaidin mhaith-good morning ","\nan raibh do lon agat?-had your lunch")
        
        elif NUMBER == 7:
            print("biodh la maith agat-have a good day","\nDia duit ar domhan-hello world","\ncad is ainm duit-What is your name?","\nmaidin mhaith-good morning ","\ngo raibh maith agat-thank you")
        elif NUMBER == 8:
            print("go raibh maith agat-thank you","\nDia duit ar domhan-hello world","\ncad is ainm duit-What is your name?")
        elif NUMBER == 9:
            print("Dia duit ar domhan - hello world","\ncad is ainm duit-What is your name?","\nmaidin mhaith-good morning ","\ngo raibh maith agat-thank you","\nbiodh la maith agat-have a good day")
        elif NUMBER == 10:
            print("Dia duit ar domhan - hello world","\ncad is ainm duit-What is your name?","\nmaidin mhaith-good morning ","\ngo raibh maith agat-thank you","\nbiodh la maith agat-have a good day")
    else:
        if NUMBER == 1:
            print("aloha honua-hello world")
        elif NUMBER == 2:
            print("O wai kou inoa?-What is your name","\naloha honua-hello world")
        elif NUMBER == 3:
            print("Aloha kakahiaka-good morning ","\naloha honua-hello world","\nO wai kou inoa?-What is your name")
        elif NUMBER == 4:
            print(" i kāu ʻaina awakea?-had your lunch?","\naloha honua-hello world","\nO wai kou inoa?-What is your name","\nAloha kakahiaka-good morning ")
        elif NUMBER == 5:
            print("maikaʻi ka hālāwai ʻana me ʻoe-nice meeting you ","\naloha honua-hello world","\nO wai kou inoa?-What is your name","\nAloha kakahiaka-good morning ","\n i kāu ʻaina awakea?-had your lunch?")
        elif NUMBER == 6:
            print("ʻoluʻolu-nice","\naloha honua-hello world","\nO wai kou inoa?-What is your name","\nAloha kakahiaka-good morning ", )
        elif NUMBER == 7:
            print("holoholona-animals","\naloha honua-hello world","\nO wai kou inoa?-What is your name","\nAloha kakahiaka-good morning ",)
        elif NUMBER == 8:
            print("ua ʻaina awakea-had lunch ","\naloha honua-hello world","\nO wai kou inoa?-What is your name","\nAloha kakahiaka-good morning ")
        elif NUMBER == 9:
            print(" he lā maikaʻi iā ʻoe-have a good day ","\naloha honua-hello world","\nO wai kou inoa?-What is your name","\nAloha kakahiaka-good morning ")
        elif NUMBER == 10:
            print("Mahalo-thank you","\naloha honua-hello world","\nO wai kou inoa?-What is your name","\nAloha kakahiaka-good morning ")

    print("you have done very well")
    time.sleep(4)

    picture_url = 'https://www.freepik.com/free-photo/excited-cheerful-stylish-caucasian-female-brunette-denim-jacket-showing-thumbs-up-smiling-delighted-approve-amazing-idea-nod-agreement-like-nice-offer-white-background_18348875.htm#fromView=search&page=1&position=34&uuid=70b9e6e1-318a-4253-a536-e12693f11aaf&new_detail=true'
    webbrowser.open(picture_url)
    time.sleep(5)
    os.system("taskkill /im msedge.exe /f")

    print("Let's know:")

    LIST = ['HOW', 'FAR', 'HAVE', 'WE', 'COME', '?']
    print(LIST[0:6])
    time.sleep(2)
    QUESTION2 = int(input("Choose 1 for YES and 2 for NO: "))
    if QUESTION2 == 1:
        x = np.linspace(1, 4, 1000)
        y = np.log(x)
        plt.plot(x, y)
        plt.xlabel('Words we learnt')
        plt.ylabel('Progress')
        plt.title('Language Learning Progress')
        plt.show()
    else:
        print("Ok, let's move on")

    print("Let's start the quiz")
    questions_and_answers = {
        1: {
            'How do you say "Hello" in Irish?': 'Dia dhuit',
            'What is the Irish word for "Goodbye"?': 'Slán',
            'How do you say "Please" in Irish?': 'Le do thoil',
            'What is the Irish phrase for "Thank you"?': 'Go raibh maith agat',
            'What is the Irish word for "Yes"?': 'Tá',
            'What is the Irish word for "No"?': 'Níl'
        },
        2: {
            'How do you say "Hello" in Hawaiian?': 'Aloha',
            'What is the Hawaiian word for "Goodbye"?': 'Aloha',
            'How do you say "Please" in Hawaiian?': 'ʻOluʻolu',
            'What is the Hawaiian word for "Thank you"?': 'Mahalo',
            'How do you say "Yes" in Hawaiian?': 'ʻAe',
            'What is the Hawaiian word for "No"?': 'ʻAʻole'
        }
    }

    selected_questions = random.sample(list(questions_and_answers[CHOICE].keys()), len(questions_and_answers[CHOICE]))
    for i, question in enumerate (selected_questions, start=1):
        print(f"{i}. {question}")
        user_answer = input("Your answer: ").strip()
        correct_answer = questions_and_answers[CHOICE][question]
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"Wrong. The correct answer is: {correct_answer}")
        print()
    time.sleep(3)    

    
    
    picture_url = 'https://in.pinterest.com/pin/753790056421755897/'
    webbrowser.open(picture_url)
    time.sleep(5)
    os.system("taskkill /im msedge.exe /f")
    
    time.sleep(2)

    repeat = input("Would you like to learn another language? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Goodbye!")
        break

