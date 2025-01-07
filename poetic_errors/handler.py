import sys
import traceback
import random
sys.stdout.reconfigure(encoding='utf-8')

class PoeticErrorHandler:
    def __init__(self):
        # Dictionary of poem templates for different error types
        self.templates = {
            'NameError': [
                ["Roses are red,", 
                 "Variables are rare,", 
                 "On line {line_num}, I looked everywhere,", 
                 "But {var_name} just wasn't there."],
                
                ["In the garden of Python,", 
                 "Where variables grow,", 
                 "I searched for {var_name},", 
                 "But it's missing, you know."]
            ],
            
            'SyntaxError': [
                ["Roses are red,", 
                 "Semicolons are fine,", 
                 "But there's something wrong,", 
                 "With the syntax on line {line_num}."],
                
                ["Your code was flowing,", 
                 "Like a sweet melody,", 
                 "Till syntax tripped up,", 
                 "On line {line_num}, you see."]
            ],
            
            'TypeError': [
                ["Roses are red,", 
                 "Types should be true,", 
                 "Can't mix {detail},", 
                 "What should I do?"],
                
                ["In the world of types,", 
                 "Everything has its place,", 
                 "But {detail},", 
                 "That's not the case."]
            ],
            
            'default': [
                ["Roses are red,", 
                 "Violets are blue,", 
                 "{error_type} occurred,", 
                 "On line {line_num}, it's true."],
                
                ["In the garden of code,", 
                 "Where bugs like to hide,", 
                 "A {error_type} appeared,", 
                 "On line {line_num}, I spied."]
            ]
        }

    def extract_error_info(self, exc_type, exc_value, tb):
        """Extract relevant information from the error."""
        error_type = exc_type.__name__
        
        # Get line number
        if tb is not None:
            line_num = traceback.extract_tb(tb)[-1].lineno
        else:
            line_num = "unknown"
            
        # Get variable name for NameError
        var_name = str(exc_value).split("'")[1] if error_type == "NameError" else None
        
        # Get error detail for TypeError
        detail = str(exc_value) if error_type == "TypeError" else None
        
        return error_type, line_num, var_name, detail

    def format_poem(self, error_type, line_num, var_name=None, detail=None):
        """Format the error as a poem."""
        # Get templates for this error type, or use default if not found
        templates = self.templates.get(error_type, self.templates['default'])
        
        # Choose a random template
        template = random.choice(templates)
        
        # Format the template with error information
        formatted_lines = []
        for line in template:
            try:
                formatted_line = line.format(
                    error_type=error_type,
                    line_num=line_num,
                    var_name=var_name,
                    detail=detail
                )
                formatted_lines.append(formatted_line)
            except KeyError:
                formatted_lines.append(line)
                
        return "\n".join(formatted_lines)

    def __call__(self, exc_type, exc_value, tb):
        """Handle the error and print the poetic message."""
        error_type, line_num, var_name, detail = self.extract_error_info(exc_type, exc_value, tb)
        poem = self.format_poem(error_type, line_num, var_name, detail)
        
        print("\nPoetic Error:🌹 ")
        print(poem)
        print("\nOriginal error:", str(exc_value))

# Install the error handler
poetic_handler = PoeticErrorHandler()
sys.excepthook = poetic_handler