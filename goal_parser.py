# finding the character after "(" to see what to add to an output string
def interpret(command):
    output = ""
    for i in range(len(command)):
        if command[i] == "G":
            output += "G"
        elif command[i] == "(":
            if command[i+1] == ")":
                output += "o"
            else:
                output += "al"
    return output

# Optimized. replacing symbols with letters

def interpret(command):
        return command.replace("()", "o").replace("(al)", "al")