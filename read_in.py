#read_in.py
from string_splitter import Split_String_Response_Output

class Read_In:
    def __init__(self):
        self.text=""
        self.split_response = Split_String_Response_Output()

    def input_from_user(self):
        text=str(input("Prompt: "))
        self.split_response.split_string_for_common_starts(text)
        return text