from pathlib import Path
"""
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)


path1 = Path('text_files/pi_digits.txt')
contents1 = path1.read_text()

for line in contents1.splitlines():
    print(line)

pi_string = ''
for line in contents1.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

path2 = Path('text_files/pi_million_digits.txt')
contents2 = path2.read_text()

pi_string1 = ''
for line in contents2.splitlines():
    pi_string1 += line.lstrip()

print(f'{pi_string1[:52]}...')
print(len(pi_string1))

birthday = input('Enter you birthday, in the form mmddyy: ')
if birthday in pi_string1:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi!')

# exercise 10.1
path3 = Path('text_files/learning_python.txt')
contents3 = path3.read_text()
print(contents3)

for line in contents3.splitlines():
    print(line)

pi_string2 = ''
for line in contents3.splitlines():
    pi_string2 += line

print(pi_string2)

contents3 = contents3.replace('python', 'C')
print(contents3)
"""
contents = 'I love programming.\n'
contents += 'I love creating new games.\n'
contents += 'I also love wroking with data.\n'

path = Path('text_files/programming.txt')
path.write_text(contents)
print(path.read_text())

#exercise 10.4, 10.5
path1 = Path('text_files/guest_book.txt')

while True:
    print("Type the guest's name or 'n' if no more guests")
    guest = input('Type your name: ')

    if guest.lower() == 'n':
        break
    
    guest_formatted = guest.title()

    # Read actual guests
    guests = path1.read_text().splitlines()

    if guest_formatted in guests:
        print('Guest already in list.')
    else:
        with open(path1, mode='a') as file:
            file.write(f'{guest_formatted}\n')


print('Follow the list of guests: ')
print(path1.read_text())
