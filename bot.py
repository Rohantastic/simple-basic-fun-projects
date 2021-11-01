import time
var = time.ctime()
questions = {
            "hi" : "Hello",
            "how are you":"I am fine! thanks for asking!!",
            "what is your name" : "am an rhos bot assistant",
            "what is time": var
    }

while True:
    inn = input()

    if(inn == "quit"):
        break

    else:
        print(questions[inn])