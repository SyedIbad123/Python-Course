# Program to greet all the person names stored in a list which starts with "S"


l1 = ["Ibad","Shahzaib","Shehzad", "Saad", "Ahsan", "Wasay"]
for item in l1:
   if item.startswith("S"):      # Here startswith functtion is used to returns a word that is startswith "S"
       print("Thank you!" + item)