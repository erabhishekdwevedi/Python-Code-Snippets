"""
Sentence Case Formatter 
 input :  String [Paragraph]
 output : String [ Paragraph Formatted in Sentence Case ]
"""
#sentence = input("Enter Sentence: ")

sentence = "this is the world.This is,awesomEtttt"
print("Original Sentence:\n", sentence)

print("Capitalize Sentence:\n", sentence.capitalize())
print("Title Sentence:\n", sentence.capitalize())

def convertToSentenceCase(sentence):

    formattedSentence = ''
    lastCharacter = ''

    for word in sentence:
        if(lastCharacter==''):
            formattedSentence = formattedSentence + word.upper()
    
        else:
            if( lastCharacter =="." or lastCharacter==","):
                formattedSentence = str(formattedSentence) + word.upper()

            else:
                formattedSentence = str(formattedSentence) + str(word).lower()
        
        lastCharacter = word
    
    print("Sentence Case:\n", formattedSentence)

convertToSentenceCase(sentence)
