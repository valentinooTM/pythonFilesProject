uczniowie = []
przedmioty = []
oceny = []

with open('uczniowie.txt') as f:
  first_line = f.readline().strip().split(";")

  lines = f.readlines()

  for line in lines:
    uczen = {}

    line = line.strip().split(";")

    uczen[first_line[0]] = line[0]
    uczen[first_line[1]] = line[1]
    uczen[first_line[2]] = line[2]
    uczen[first_line[3]] = line[3]
    uczen[first_line[4]] = line[4]
    uczen[first_line[5]] = line[5]

    uczniowie.append(uczen)


with open('przedmioty.txt') as f:
  first_line = f.readline().strip().split(";")
  first_line.pop()

  lines = f.readlines()

  for line in lines:
    przedmiot = {}

    line = line.split(";")

    przedmiot[first_line[0]] = line[0]
    przedmiot[first_line[1]] = line[1]
    przedmiot[first_line[2]] = line[2]
    przedmiot[first_line[3]] = line[3]

    przedmioty.append(przedmiot)

with open('oceny.txt') as f:
  first_line = f.readline().strip().split(";")

  lines = f.readlines()

  for line in lines:
    ocena={}

    line = line.strip().split(";")

    ocena[first_line[0]] = int(line[0])
    ocena[first_line[1]] = int(line[1])
    ocena[first_line[2]] = line[2]
    ocena[first_line[3]] = int(line[3])

    oceny.append(ocena)


print(oceny)