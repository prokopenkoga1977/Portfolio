def ask_operation():
        operation = input("""
        +) Sum 
        -) Subtruction  
        *) Multiply
        /) Divide
        **) Square
        
    Answer : """)
        
        correct_operations=['+', '-', '*', '/', '**']
        while operation not in correct_operations:
            print("Incorrect operation. Repeat the operation from the list")
            operation = input("""
        +) Sum 
        -) Subtruction  
        *) Multiply
        /) Divide
        **) Square
        
    Answer : """)
             
        return operation
 
        