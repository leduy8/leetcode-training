# * https://leetcode.com/problems/goal-parser-interpretation/

def interpret(command: str) -> str:
    interpreted = ""

    for i in range(len(command)):
        if command[i] == "G":
            interpreted += "G"
        elif command[i] == "(":
            if command[i + 1] == ")":
                interpreted += "o"
                i += 2
            else:
                interpreted += "al"
                i += 4

    return interpreted


print(interpret(command="G()(al)"))  # Goal
print(interpret(command="G()()()()(al)"))  # Gooooal
print(interpret(command="(al)G(al)()()G"))  # alGalooG
