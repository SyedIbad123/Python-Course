# Program to remove a given word from list and strip it at the same time..

def remove(string,word):
    new_str = string.replace(word, "")
    return new_str.strip()

string = "Ibad is the student of software       engineering"
n = remove(string,"software")
print(n)