# -*- coding: utf-8 -*-
print "Welcome to the PygLatin"
pyg = 'ay'  #Wird ans Word angehängt

original = raw_input('Enter a word:')  #Eingabe des Wortes
word = original.lower()  #großbuchstaben werden entfernt

if len(
        original) > 0 and original.isalpha():  #Es wird überprüft ob ein wort eingeben wurde und ob es nur Buchstaben sind
    print original  #Word wird ausgegeben
else:  #Wenn nichts dort steht
    print 'empty'  #Ausgabe empty

first = word[0]  #Es wird der erste Buchstabe Selektiert

new_word = word[1:] + first + pyg  #Word wird neu zusammen gestellt
print new_word  #Ausgabe des neuen wortes
