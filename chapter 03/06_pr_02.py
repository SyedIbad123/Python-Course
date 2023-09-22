# write a program to customize letter..



Letter = ''' Dear <|Name|>
Congratulations, You have won the prize.

Dated : <|Date|>
'''
name = input("enter your name \n")
date = input("enter date \n")
Letter = Letter.replace ("<|Name|>", name)
Letter = Letter.replace ("<|Date|>", date)
print(Letter)