import pyttsx3
if __name__=="__main__":
    print("Welcome to Robo Speaker 1.1 created by Mirza Shahrukh Beg")
    engine = pyttsx3.init()
    while True:
        x = input("Write what you want to speak: ")
        if x=="q":
            break
        engine.say(x)
        engine.runAndWait()

