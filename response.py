#response.py
from replace_words import Replace_Words

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