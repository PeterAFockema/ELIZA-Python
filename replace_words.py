#replace_words.py

class Replace_Words:
    def __init__(self):
        self.text_to_replace=""

    def replaced_text(self, text_to_replace):
        self.text_to_replace=text_to_replace.replace("you","I")
        self.text_to_replace=self.text_to_replace.replace("my", "your")
        self.text_to_replace=self.text_to_replace.replace(" me"," you")
        self.text_to_replace= self.text_to_replace.replace("I am","you are")
        self.text_to_replace= self.text_to_replace.replace("I'm","you are")
        self.text_to_replace=self.text_to_replace.replace("am","are")
        self.text_to_replace= self.text_to_replace.replace("I've", "you have")
        self.text_to_replace= self.text_to_replace.replace("I have", "you have")
        self.text_to_replace= self.text_to_replace.replace("I can", "you can")
        self.text_to_replace= self.text_to_replace.replace("I was", "you were")
        self.text_to_replace= self.text_to_replace.replace("I shall", "you shall")
        self.text_to_replace= self.text_to_replace.replace("I will", "you will")
        self.text_to_replace= self.text_to_replace.replace("I really", "you really")
        self.text_to_replace= self.text_to_replace.replace("if I", "if you")
        self.text_to_replace= self.text_to_replace.replace("like I", "like you")
        self.text_to_replace= self.text_to_replace.replace("I could", "you could")
        self.text_to_replace= self.text_to_replace.replace("I would", "you would")
        self.text_to_replace= self.text_to_replace.replace("I might", "you might")
        return self.text_to_replace
