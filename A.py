import nltk
import sys

greeting = sys.stdin.read()
print (greeting)

token_list = nltk.word_tokenize(greeting)
print ("The tokens in the greeting are")

wolf = 0
lion = 0
for token in token_list:
    if(token.lower() == "wolf"):
        wolf += 1
    elif(token.lower() == "lion"):
        lion += 1
    print (token)

print("There were %d instances of the word 'lion' and %d instances of the word 'wolf'" % (lion, wolf))
