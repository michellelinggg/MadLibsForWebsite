#!/usr/bin/python

import cgitb                   
cgitb.enable()
import urllib
import string
import random

import cgi
form = cgi.FieldStorage()

firstc = form['firstvalue'].value 
secondc = form['secondvalue'].value 
thirdc = form['thirdvalue'].value 
fourthc = form['fourthvalue'].value 
fifthc = form['fifthvalue'].value 
choices = form['choicesmade'].value 
choices = choices.split()
nounsinstory = ["princess", "admirers", "dragon", "horse"]
adverbsinstory = ["quickly", "loudly", "immediately"]
smellsinstory = ["sweet", "fantastic", "that bad"]
verbsinstory = ["stand", "eat", "sing"]
adjectivesinstory = ["beautiful", "perfect", "curious"]
namesinstory = ["Daisy", "ChaCha", "Melvin"]
nouns = []
adverbs = []
smells = []
verbs = []
adjectives = []
names = []

def placeInOrder(number, item):
	if item == "Noun:":
		whichItem(number, nouns)
	elif item == "Adjective:":
		whichItem(number, adjectives)
	elif item == "Verb:":
		whichItem(number, verbs)
	elif item == "Adverb:":
		whichItem(number, adverbs)
	elif item == "Smell:":
		whichItem(number, smells)
	else:
		whichItem(number, names)
		

def whichItem(number, item):
	if number == 1:
		item.append(firstc)
	elif number == 2:
		item.append(secondc)
	elif number == 3:
		item.append(thirdc)
	elif number == 4:
		item.append(fourthc)
	else:
		item.append(fifthc)

counter = 1
for item in choices:
	placeInOrder(counter, item)
	counter += 1

f = open("madlibs.rtf", "r")
theStory = f.read()
f.close()

def replaceStoryWords(transferlist, originallist):
	global theStory
	if not transferlist:
		return None
	elif transferlist == names:
		for item in transferlist:
			if not originallist:
				return None
			replaced = random.choice(originallist)
			originallist.remove(replaced)
			theStory = theStory.replace(replaced, "<span id='replaced'>" + item.title() + "</span>")
	else:
		for item in transferlist:
			if not originallist:
				return None
			replaced = random.choice(originallist)
			originallist.remove(replaced)
			theStory = theStory.replace(replaced, "<span id='replaced'>" + item + "</span>")

replaceStoryWords(names, namesinstory)
replaceStoryWords(verbs, verbsinstory)
replaceStoryWords(adverbs, adverbsinstory)
replaceStoryWords(adjectives, adjectivesinstory)
replaceStoryWords(nouns, nounsinstory)
replaceStoryWords(smells, smellsinstory)

print 'Content-Type: text/html'
print 
print '<html>'
print '<head>'
print '<title>Dis shit crazy yo</title>'
print '<link rel="stylesheet" href="madlibstory.css" />'
print '<link href="http://fonts.googleapis.com/css?family=Gochi+Hand" rel="stylesheet" type="text/css">'
print '</head>'
print '<h1>The Worst FairyTale Disney Never Told</h1>'
print '<body>'
print theStory
print '<br/><br/><img id="picture" src="http://i.imgur.com/otLw3an.jpg"/></body>'
print '<h3>-THE END-</h3>'
print '<br/><br/>'
print '<button id="playbutton" type="button" onclick="beginGame()">Play Again?</button>'
print '</html>'