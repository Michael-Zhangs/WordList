import json
import os
import math

clear = "clear"
filename = "wordlist.json"

active = True

def get_list():
	try:
		with open(filename) as f_obj:
			wordlist = json.load(f_obj)
	except FileNotFoundError:
		wordlist = []
	while True:
		word={
			"En":"", #English
			"Tr":"", #Translation
			"ti":0,  #times
			"cr":0,  #correct
		}
		tmp = input("word:")
		if tmp == "q":
			break
		flag=False
		for single_word in wordlist:
			if single_word["En"] == tmp:
				print("The word has already in the list!")
				input()
				flag=True
				break
		if flag:
			continue
		word["En"]=tmp
		word["Tr"]=input("Translation:")
		wordlist.append(word)
	with open(filename, 'w') as f_obj:
		json.dump(wordlist, f_obj)
		

def edit_list():
	try:
		with open(filename) as f_obj:
			wordlist = json.load(f_obj)
	except FileNotFoundError:
		print("No list is recorded")
		input()
		return
	page = 0
	set_default = 10
	page_all = math.ceil(len(wordlist) / set_default)
	while True:
		os.system(clear)
		if page*set_default+10 > len(wordlist):
			line_tmp = len(wordlist) - page*set_default
		else:
			line_tmp = set_default
		for line in range(0,line_tmp):
			print(wordlist[page*set_default+line]["En"]+"\t"+
				wordlist[page*set_default+line]["Tr"]+"\t"+
				"times: "+str(wordlist[page*set_default+line]["ti"])+"\t"+
				"correct: "+str(wordlist[page*set_default+line]["cr"]))
		for line in range(0,10-line_tmp):
			print()
		print("\n\t\t"+"Page: "+str(page)+"/"+str(page_all-1))
		cmd = input()
		if cmd == "n":
			if page<page_all-1:
				page=page+1
		if cmd == "l":
			if page>0:
				page=page-1
		if cmd == "q":
			return


def exercise():
	print("exercise")
	input()

def quit():
	global active
	active = False

def default():
	print("No such a selection")
	input()

def main_menu():
	print("1.Get List")
	print("2.Edit List")
	print("3.Exercise")
	print("4.Quit")
	choice = input()
	choice = int(choice)
	switch={	
		1:get_list,
		2:edit_list,
		3:exercise,
		4:quit,
	}
	os.system(clear)
	switch.get(choice, default)()

while active:
	os.system(clear)
	main_menu()
