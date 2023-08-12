#My first version
terms_of_fibonacci = int(input())

counter = 0
current = 0
next = 1

while counter < terms_of_fibonacci - 1:
    print(f'{current}, ', end='')
    counter += 1
    later = current + next
    current = next
    next = later
print(f'{next}')

#-------------------------------------------

#My second version
terms_of_fibonacci = int(input())

counter = 1
current = 1
next = 1
print(f'0', end='')
while counter < terms_of_fibonacci:
    print(f', {current}', end='')
    counter += 1
    later = current + next
    current = next
    next = later

#----------------------------------------

#ChatGPT correction (eliminates de var 'later'):

#correction of first code
terms_of_fibonacci = int(input())

counter = 0
current = 0
next = 1

while counter < terms_of_fibonacci - 1:
    print(f'{current}, ', end='')
    counter += 1
    current, next = next, current + next  # Isso faz a atualização de current e next simultaneamente
print(f'{current}')


#correction of second code
terms_of_fibonacci = int(input())

counter = 1
current = 0
next = 1

print(f'{current}', end='')
while counter < terms_of_fibonacci:
    print(f', {next}', end='')
    counter += 1
    current, next = next, current + next
''''''