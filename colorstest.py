from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
import random
import time


def whatcolor(i):
    if i==0:
        print(Back.BLACK)
        print('0')
    if i==1:
        print(Back.RED)
        print('1')
    if i==2:
    	print(Back.GREEN)
    	print('2')
    if i==3:
    	print(Back.YELLOW)
    	print('3')
    if i==4:
    	print(Back.BLUE)
    	print('4')
    if i==5:
    	print(Back.MAGENTA)
    	print('5')
    if i==6:
    	print(Back.CYAN)
    	print('6')
    if i==7:
    	print(Back.WHITE)
    	print('7')

#print(Style.BRIGHT)

for i in range(10):
	for i in range(8):
		print(Style.BRIGHT)
		whatcolor(random.randint(0,7))
	print(Style.RESET_ALL)
	print('***')
	time.sleep(1)
print(Style.RESET_ALL)

"""
print('--> FIRST LINE')

print(Back.CYAN)
print(Back.GREEN)
print(Back.RED)
print(Back.WHITE)
print(Back.BLUE)
print(Back.YELLOW)
print(Back.BLACK)
print(Back.MAGENTA)

print(Style.RESET_ALL)
print('--> LAST LINE')
"""

#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a greenbackground')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
#print()
