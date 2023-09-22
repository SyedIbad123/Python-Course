# Program to censored abusive words that are written in file..


with open('sample.txt') as f:
    content = f.read()

content = content.replace("donkey",'!@#$$%^&*%')

with open('sample.txt', 'w') as f:
    f.write(content)