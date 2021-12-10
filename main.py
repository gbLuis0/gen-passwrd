#!/bin/python3
from random import choice
from os import system

#cores
amare = "\033[93;1m"
ver = "\033[92;1m"
verm = "\033[91;1m"
a = "\033[94;1m"
n = "\033[1m"
f = "\033[m"

#caracteres para senha
maiu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minu = 'abcdefghijklmnopqrstuvwxyz'
carct = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
num = '1234567890'
senha = str()

def clear():
    system('cls||clear')

def dicas():
    clear()
    print(f'''{ver}Algumas dicas sobre senhas fortes:\n
    \t\t1. {verm}Aleatoriedade{f}\n{n}É fundamental uma senha ter aleatoriedade, ou seja,\nnão seguir um padrão de dígitos\ncomo por exemplo: "{amare}qwert{f}{n}", é uma sequência de letras do teclado,\ne não possui aleatoriedade\noutro exemplo: "{amare}sfj438ebs834bf{f}{n}", não é uma sequência,\npossuindo assim, aleatoriedade.\n 
    \t\t{ver}2.{f}{verm} Dados pessoais{f}\n{n}Um erro muito comum das pessoas em relação às suas senhas\né colocar dados pesoais como idade, data de nascimento e nome.\nSão falhas que podem correr em risco a sua conta,\ne consequentemente, você.\n
    \t\t{ver}3. {verm}Caracteres{f}\n{n} Ter variados tipos de caracteres na sua senha, maiúsculas ({amare}A{f}{n} - {amare}Z{f}{n}),\nminúsculas ({amare}a{f}{n} - {amare}z{f}{n}), números ({amare}0{f}{n} - {amare}9{f}{n}) e símbolos ({amare}-_=+[^><{f}{n} ...)\ntambém é fundamental para uma senha segura e mais difícil de ser quebrada.\nSem falar do tamanho da senha, para ser considerada "segura"\né recomendado ter no minímo 8 caracteres.\nRecomendo que sua senha não seja tão pequena pra não ser fácil de quebra-la,\ne nem tão grande para não ser difícil de lembrar ou digitar.\n''')

#nível da senha
def facil(l):
	senha = str()
	items = [minu, num]
	for c in range(l):
		senha += choice(choice(items))
	return senha

def normal(l):
	senha = str()
	while len(senha) != l:
		items = [minu, maiu, num]
		ca = choice(items)
		senha += choice(ca)
		if len(senha) == l: break
		items.remove(ca)
		ca = choice(items)
		senha += choice(ca)
	return senha

def dificil(l):
	senha = str()
	while len(senha) != l:
		items = [minu, maiu, num, carct]
		ca =  choice(items)
		senha += choice(ca)
		if len(senha) == l: break
		items.remove(ca)
		ca = choice(items)
		senha += choice(ca)
		if len(senha) == l: break
		items.remove(ca)
		ca = choice(items)
		senha += choice(ca)
	return senha

per = 's'
while per == 's':
    clear()
    opc = '6'
    try:
        while not opc in '12345':
            clear()
            opc = input(f'''{ver}!{amare}Escolha como será a sua senha{ver}!{f}
{n}[ {ver}1{f}{n} ] > {ver}Fácil{f}\n{n}[ {ver}2{f}{n} ] > {ver}Normal{f}\n{n}[ {ver}3{f}{n} ] > {ver}Difícil{f}\n\n{n}[ {ver}4{f}{n} ] > {ver}Dicas{f}\n{n}[ {ver}5{f}{n} ] > {ver}Sair{f}\n\n{n}>>>{f} ''').strip()[0]
    except:
        continue
    match opc:
        case '1':
            l = int(input(f'{n}Número de caracteres da sua senha:{f} ').strip())
            senha = facil(l)
            print(f'{n}Senha:{f}\n{senha}')
        case '2':
            l = int(input(f'{n}Número de caracteres da sua senha:{f} ').strip())
            senha = normal(l)
            print(f'{n}Senha:{f}\n{senha}')
        case '3':
            l = int(input(f'{n}Número de caracteres da sua senha:{f} ').strip())
            senha = dificil(l)
            print(f'{n}Senha:{f}\n{senha}')
        case '4':
            dicas()
        case '5':
            break
    if opc in '123':
        sal = input(f'{n}Quer salvar a senha? [{a}s{f}/{a}n{f}{n}]{f} ').strip().lower()[0]
        if sal == 's':
            nome = input(f'{n}Nome do arquivo: ({amare}espaços serão substituídos por -{f}{n}){f} ').strip()
            if '  ' in nome: nome = nome.replace('  ', '-')
            if ' ' in nome: nome = nome.replace(' ', '-')
            system(f'cd senhas && touch {nome}.txt && echo {senha} >> {nome}.txt')
            print(f'{ver}Senha salva, confira a pasta "senhas"!{f}')
    try:
        per = input(f'{n}Deseja gerar uma nova senha? [{a}s{f}/{a}n{f}{n}]{f} ').strip().lower()[0]
    except:
        continue
system('cls||clear')
print(f'{a}Obrigado por usar meu script!\nNão se esqueça de avalia-lo e até mais :){f}')
