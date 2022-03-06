path = '//home//daro//Python//zad3//zadanie3//rolling_stones.txt'

with open (path, 'r') as file:
  content2 = file.read()
  file.close()

with open(path, 'r') as file:
  content = file.readlines()
  file.close()

content = str(content[0])


def usun_kropki(content):

  x = content.replace(".", "")
  return x

def usun_przecinki(content):

  x = content.replace(",", "")
  return x

def duze_na_male(content):

  x = content.lower()
  return x

def razem(content):
  listRes = list(content.split(" "))
  return listRes

def liczy_liczbe_roznych_slow(content):
  x = len(razem(content))
  return x

def ile_a(content):
  char = str('a')
  count = 0
  for c in content:
    if char == c:
      count += 1
  return count


def ile(content, x):
  char = str(x)
  count = 0
  for c in content:
    if char == c:
      count += 1
  return count

#funkcja usuwajaca kropki
print(usun_kropki(content))

#funkcja usuwajaca przecinki
print(usun_przecinki(content))

#funkcja zamienia duze na male
print(duze_na_male(content))

#funkcja liczy liczbe roznych slow
print(liczy_liczbe_roznych_slow(content))

# #funkcja licząca ilość wystapień litery "a"     "ile_a"
print('Litera "a" wystepuje ', ile_a(content),' razy')
#
#funkcja licząca ilość wystapień wskazanej litery     "ile"
x = input('podaj liczbe do policzenia: ')
print('Litera ' ,x, ' wystepuje ', ile(content, x),' razy')
#
#funkcja biorąca "content" i zapisująca wszystkie linie w jednej liście     "razem"
content_razem = razem(content)
print(content_razem)


