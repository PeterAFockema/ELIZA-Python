#eliza.py
import random

from read_in import Read_In

class Eliza:
    def __init__(self):
        self.initials= ["Hello, how are you?", "Howdy! How's it going?", "Hey! What's up?", "Yo! How are things?", "Hi. What do you want to talk about?"]
        self.finals= ["Actually, I'm beat, let's chat later.", "I've got to go, let's talk another time!", "Hold that thought- let's chat in a bit."]
        self.read_in = Read_In()

    def initial(self):
        return random.choice(self.initials)

    def input_from_user(self):
        text=self.read_in.input_from_user()
        return text

    def run_eliza(self):
        print("ELIZA: " + self.initial())
        i = 0
        while(i<=10):
            text=self.input_from_user()
            i=i+1
        print("ELIZA: " + random.choice(self.finals))

def main():
    eliza = Eliza()
    eliza.run_eliza()

if __name__ == '__main__':
    main()