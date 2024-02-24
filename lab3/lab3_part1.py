import os # for working with the file system
import uuid # for generating unique ids
import json # for saving data to text
import time # for generating a timestamp

# this class encapsulates the idea of a survey question, including the question processing (validation) any logic that would have the question be skipped
# this could be even more powerful if there were a list of validation functions, allowing for composite validations
class Question:
    def __init__(self, title, prompt, default_value, validation_func = None, skip_logic = None):
        self.prompt = prompt
        self.validation_function = validation_func
        self.skip_logic = skip_logic
        self.default_value = default_value
        self.title = title
        self.value = self.default_value
        self.entry_time = None


    # the question can run itself
    def run(self):
        self.entry_time = time.time() # this is system time as a float
        if self.skip_logic and self.skip_logic():
            return
        while True: 
            text = input(self.prompt)
            if self.validation_function: # if it has a validation function, we need to process the data with it
                res, data = self.validation_function(text)
                if res: # this means that the data is valid
                    self.value = data # good data from the validation function
                    return
                else: # this means that the data is an error message
                    print(data) # the error message
            else:
                self.value = text # we don't need to validate
                return
# this is an app-specific class representing a specific form including Question objects
class MyForm:
    def __init__(self):
        self.__valid_degree_types = ["undergraduate","masters","doctorate"]
        self.questions = [
            Question("Name",
                     "Enter your name (family name, given name): ",
                     ["Doe","Jane"],
                     self.name_validation),
            Question("Age", 
                     "Enter your age as a single, whole number (e.g., 42).  If you prefer to leave this blank, enter -1: ",
                     -1, 
                     self.age_validation),
            Question("Current Degree", 
                     f"Enter your current degree type ({','.join([x for x in self.__valid_degree_types])}): ", 
                     self.__valid_degree_types[0], 
                     self.degree_type_validation),
            Question("Prior Institutions", 
                     "Enter any past institutions you have attended (separate multiple entries with a comma, e.g., University of Georgia, Penn State University): ", 
                     [], 
                     self.institution_validation),
            Question("Programming Experience",  
                     "Enter your level of programming experience on a scale from 0 (none, like Steve Jobs) to 10 (expert, like John Carmack): ", 
                     0, 
                     self.experience_validation),
            Question("Comment", 
                     "Provide a short description of where you obtained that experience: ", 
                     "", 
                     lambda x: (True,x) if len(x) > 0 else (False,"You must enter something."),  # note, for consistency, I would probably put these down below
                     lambda: True if self.questions[4].value == 0 else False) # but, I wanted to showcase lambdas in the solution
        ]
    def name_validation(self, text):
        if "(" in text or ")" in text:
            return False, "Please do not use parentheses: Doe,Jane instead of (Doe,Jane)"
        parts = [x.strip() for x in text.split(",")] # get rid of any leading or trailing whitespace between commas
        if len(parts) != 2:
            return False, "You must separate your name as (family name, given name): Doe,Jane not Jane Doe.  If you only have a given name, enter it as ,Jane"
        if len(parts[1]) == 0:
            return False, "You can't have a blank given name"
        return True, parts
    
    def age_validation(self, text):
        try:
            age = int(text)
        except:
            return False, "Invalid whole number"
        if age < -1:
            return False, "Invalid negative number"
        return True, age
    
    def degree_type_validation(self, text):
        if text not in self.__valid_degree_types:
            return False, "Invalid entry"
        return True, text
    
    def institution_validation(self, text): # there's not much to validate here
        parts = [x.strip() for x in text.split(",")]
        return True, parts
    
    def experience_validation(self, text):
        try:
            experience = int(text)
        except:
            return False, "This must be an integer."
        
        if experience < 0 or experience > 10:
            return False, "The number must be from 0 to 10"
        
        return True, experience
                
    def run(self):
        for q in self.questions:
            q.run()
        
        print("You entered the following information")
        for q in self.questions: 
            print(q.title,": ",q.value)
            
        os.makedirs("data",exist_ok=True)
        with open("data/"+str(uuid.uuid4())+".json","w") as f: #this creates a new json file as a unique id
            f.write(json.dumps({q.title:{"answer":q.value,"time":q.entry_time} for q in self.questions})) # this writes out the relevant details

# this makes my classes importable
if __name__=="__main__":
    form = MyForm()
    form.run()

        