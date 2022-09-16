#string_splitter.py
import random
import re
from replace_words import Replace_Words
from response import Response

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