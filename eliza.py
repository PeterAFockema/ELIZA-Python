#eliza.py
import random
import sys
import re

class Replace_Words:
    def __init__(self):
        self.text_to_replace=""

    def replaced_text(self, text_to_replace):
        self.text_to_replace=text_to_replace.replace("you","I")
        self.text_to_replace=self.text_to_replace.replace("my", "your")
        self.text_to_replace=self.text_to_replace.replace(" me"," you")
        self.text_to_replace= self.text_to_replace.replace("I am","you are")
        self.text_to_replace= self.text_to_replace.replace("I've", "you have")
        self.text_to_replace= self.text_to_replace.replace("I have", "you have")
        self.text_to_replace= self.text_to_replace.replace("I can", "you can")
        self.text_to_replace= self.text_to_replace.replace("if I", "if you")
        self.text_to_replace= self.text_to_replace.replace("like I", "like you")
        self.text_to_replace= self.text_to_replace.replace("I could", "you could")
        self.text_to_replace= self.text_to_replace.replace("I would", "you would")
        self.text_to_replace= self.text_to_replace.replace("I might", "you might")
        return self.text_to_replace

class Response:
    def __init__(self):
        self.return_query=""
        self.descriptive_emotions=["feel", "want", "love", "hate", "think"]
        self.replace_words=Replace_Words()

    def return_response(self, descriptive_emotion, context_of_discussion):
        try:
            self.return_query="Why do you "
            t=self.descriptive_emotions.index(descriptive_emotion)
            context_of_discussion = self.replace_words.replaced_text(context_of_discussion)
            self.return_query = self.return_query + descriptive_emotion + " "+ context_of_discussion + "?"
        except IndexError:
            print("ELIZA: I don't know this feeling of " + descriptive_emotion)
            self.return_query = ""
        return self.return_query

class Split_String_Response_Output:
    def __init__(self):
        self.initial_phrase= ["I feel ", "I want ", "I love ", "I hate ", "I think "]
        self.continuing_phrase = ["Tell me more.", "Go on!", "Talk to me more about your feelings about this.", "Do you love or hate that?"]
        self.split_line_array = []
        self.single_expression= ""
        self.point_of_discussion = ""
        self.response = Response()

    def split_string_for_common_starts(self, line_to_split):
        term_exists = 0
        try:
            y = 0
            for x in self.initial_phrase:
                y = y + 1
                if (x in line_to_split):
                    self.split_line_array = re.split(self.initial_phrase[y-1], line_to_split, 1)
                    self.point_of_discussion = str(self.split_line_array)
                    self.single_expression = re.split("I ", self.initial_phrase[y-1], 2)
                    self.single_expression = str(self.single_expression[1]).replace(" ","")
                    print("ELIZA: "+self.response.return_response(self.single_expression, self.split_line_array[1]))
                    term_exists = 1
                    return self.split_line_array
        except IndexError:
            print("")

        if (term_exists == 0):
            print("ELIZA: "+ random.choice(self.continuing_phrase))

class Read_In:
    def __init__(self):
        self.text=""
        self.split_response = Split_String_Response_Output()

    def input_from_user(self):
        text=str(input("Prompt: "))
        self.split_response.split_string_for_common_starts(text)
        return text

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