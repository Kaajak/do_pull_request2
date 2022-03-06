path = "C://Users//vdi-student//PycharmProjects//123//zadanie3//rolling_stones.txt"
with open (path, 'r') as file:
    content = file.readlines()
with open (path, 'r') as file:
    content2 = file.read()

content = str(content[0])

def usuwa_przecinki(content):
    bezprzecinka = content.replace(",", " ")
    return bezprzecinka

#print(usuwa_przecinki(content))

def usuwa_kropki(content):
    bezkropki = content.replace(".", "")
    return bezkropki

#print(usuwa_kropki(content))

def male_znaki(content):
    lower = content.lower()
    return lower

#print(male_znaki(content))



