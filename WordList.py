import json
import os

wordlist={}
word={
	"English":"",
	"Chinese":"",
	"times":"",
	"correct":""
}

active = True

def get_list():
	print("get list")
	input()

def edit_list():
	print("edit list")
	input()

def save_data():
	print("save data")
	input()

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
	print("3.Save Data")
	print("4.Exercise")
	print("5.Quit")
	choice = input()
	choice = int(choice)
	switch={	
		1:get_list,
		2:edit_list,
		3:save_data,
		4:exercise,
		5:quit,
	}
	os.system("clear")
	switch.get(choice, default)()

while active:
	main_menu()
	os.system("clear")
