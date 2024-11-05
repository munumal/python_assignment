
word_list = ["Hello","world","python","is","amazing"]


def add_exclamation(strings):
    for i in range (len(strings)):
        strings[i] += "!"
        
#use case        
add_exclamation(word_list)
#print(word_list)


def add_exclamation(strings):
    return [string + "!" for string in strings]

#use case 
new_list= add_exclamation(word_list)
print(f"New list = {new_list}")
print(f"Original list = {word_list}")