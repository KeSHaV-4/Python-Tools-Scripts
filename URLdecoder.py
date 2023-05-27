

print('''          _______  _          ______   _______  _______  _______  ______   _______  _______ 
|\     /|(  ____ )( \        (  __  \ (  ____ \(  ____ \(  ___  )(  __  \ (  ____ \(  ____ )
| )   ( || (    )|| (        | (  \  )| (    \/| (    \/| (   ) || (  \  )| (    \/| (    )|
| |   | || (____)|| |        | |   ) || (__    | |      | |   | || |   ) || (__    | (____)|
| |   | ||     __)| |        | |   | ||  __)   | |      | |   | || |   | ||  __)   |     __)
| |   | || (\ (   | |        | |   ) || (      | |      | |   | || |   ) || (      | (\ (   
| (___) || ) \ \__| (____/\  | (__/  )| (____/\| (____/\| (___) || (__/  )| (____/\| ) \ \__
(_______)|/   \__/(_______/  (______/ (_______/(_______/(_______)(______/ (_______/|/   \__/ 
Made By: Keshav Thakur  {GitHub Profile-->KeSHaV-4}''')
# Prompt the user for input
user_input = input("Enter a string with URL encoded characters: ")

# Replace URL encoded characters
'''im decoding all encoded special character,
 this will helps us to identify which payload attacker are using'''

replaceALL = {
    '%20': ' ',
    '+': ' ',
    '%21': '!',
    '%22': '"',
    '%23': '#',
    '%24': '$',
    '%25': '%',
    '%26': '&',
    '%27': "'",
    '%28': '(',
    '%29': ')',
    '%E2%82%AC': '€',
    '%C2%A3' : '£',
    '%C2%A9': '©',
    '%C2%AE': '®',
    '%C3%80': 'À',
    '%C3%81': 'Á',
    '%C3%82': 'Â',
    '%C3%83': 'Ã',
    '%C3%84': 'Ä',
    '%C3%85': 'Å',
    '%2C': ',',
    '%3D': '=',
    '%2A': '*',
    '%2D': '-',
    '%2E': '.',
    '%2F': '/',
    '%3A': ':',
    '%3B': ';',
    '%3C': '<',
    '%3E': '>',
    '%3F': '?',
    '%7C': '|',
    '%7B': '{',
    '%7D': '}',
    '%7E': '~',
    '%5B': '[',
    '%5D': ']',
    '%5E': '^',
    '%5C': '\\'
        
        
}

#writing a for loop to replace all Hexa code into Normal Letter 
for code, symbol in replaceALL.items():
    user_input = user_input.replace(code, symbol)

# Print the output 
print("Output:", user_input)
