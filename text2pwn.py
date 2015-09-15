#!/usr/bin/python
# coding: utf8
#text2pwn by knt
import sys
from urllib import urlencode
#///////////print///////////
#print "Text2Pwn"
def gfxpa():
	print " "
	uno = ('╔══════════kounterfeit@github════════╗')
	dos = ('║                                    ║')
	tres = ('║              Text2Pwn              ║')
	cuatro = (' ║                                    ║ ')
	cinco = ('╚══════════MD5═Base64═URL═HEX════════╝')
	print uno.center(120, ' ')
	print dos.center(84, ' ')
	print tres.center(83, ' ')
	print cuatro.center(84, ' ')
	print cinco.center(125, ' ')
gfxpa()
#/////////ENCODERS//////////
#URL Encoding
def urlenc():
	
	#pr2 =" text2pwn"
	
	#print pr2.center(80, ' ')
	c = raw_input("Input: ")
	s = c
	print ""
	salida = urlencode({'Encoded':s})
	print salida
#urlenc()

#Base64
def base():
	from base64 import b64encode
	inp = raw_input("Input: ")
	enc = b64encode(inp)
	print " "
	print "Base 64: " + enc
#base()

#md5
def md5():
	from md5 import md5
	inp = raw_input("Input: ")
	xx = md5(inp).hexdigest()
	print " "
	print "MD5 Hash: " + xx
#md5()

#HEX
def hexa():
	inp = raw_input("Input: ")
	hexx = inp.encode("hex")
	print " "
	print "HEX: " + hexx.upper()
#hexa()	

#//////////MAIN/////////////
def main():
	print " "
	resp = raw_input("Choose your encode: ")
	print " "
	if resp == "md5":
		for _ in range(100):
			print " "
			md5()
	elif resp == "base64":
		for _ in range(100):
			print " "
			base()
	elif resp == "hex":
		for _ in range(100):
			print " "
			hexa()
	elif resp == "url":
		pr = "----URL+ENCODER----"
		print pr.center(80, ' ')
		for _ in range(100):
			print " "
			urlenc()
	elif resp == "top":
			main()
	else:
		print "Bad input."
		sys.exit()
for _ in range (100):
	main()

