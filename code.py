from time import sleep

import keyboard

r=r'C:\Users\hansc\Downloads\shortcuts.txt'
with open(r,mode='r',encoding='utf-8') as f:
    data=f.read()
print(data)
codeops=[x.split(',',maxsplit=1) for x in data.strip().splitlines()]
pr='@'
for code in codeops:
    keyboard.add_abbreviation(f'{pr}{code[0]}',
    code[1].replace(r'\\', '\\').replace('\\n', '\n'))

while (g:=input() !='exit'):
    sleep(1)

