def morse_code(message):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    translator = {}
    transformations = []
    for i in range(len(morse)):
        translator[alphabet[i]] = morse[i]
    for i in range(len(message)):
        new_transformations = ""
        for j in range(len(message[i])):
            new_transformations += translator[message[i][j]]
        
        transformations.append(new_transformations)
    
    transformations = dict.fromkeys(transformations)
    print(len(transformations))

if __name__ == "__main__":
    message = ["gin","zen","gig","msg"]
    morse_code(message)