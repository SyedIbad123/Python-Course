# Program to create a dict of urdu words with values  as their english translation. Provide the user with an option to look it up!....

myDict = {
    "pankkha":"fan",
    "dabba":"box",
    "haath":"hand"
}
print("Options are ", myDict.keys())
a = input("Enter the Urdu word\n")
print("The meaning of your word is : ", myDict[a])

# To avoid from an error we use get method of dictionary..
print("The meaning of your word is : ", myDict.get(a))

