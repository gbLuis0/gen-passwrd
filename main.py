#!/bin/python3
from random import choice
from os import system

#cores
amare = "\033[93;1m"
ver = "\033[92;1m"
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

#script rodando
per = 's'
while (per == 's'):
    clear()
    opc = '5'
    while not opc in '1234':
        clear()
        try:
            opc = input(f'''{ver}!{amare}Escolha como será a sua senha{ver}!{f}
{n}[ {ver}1{f}{n} ] > {ver}Fácil{f}\n{n}[ {ver}2{f}{n} ] > {ver}Normal{f}\n{n}[ {ver}3{f}{n} ] > {ver}Difícil{f}\n\n{n}[ {ver}4{f}{n} ] > {ver}Sair{f}\n\n{n}>>>{f} ''').strip()[0]
        except:
            continue
    l = int(input(f'{n}Número de caracteres da sua senha:{f} ').strip())
    match opc:
        case '1':
            senha = facil(l)
            print(f'{n}Senha:{f}\n{senha}')
        case '2':
            senha = normal(l)
            print(f'{n}Senha:{f}\n{senha}')
        case '3':
            senha = dificil(l)
            print(f'{n}Senha:{f}\n{senha}')
    if opc == '4': break

    sal = input(f'{n}Quer salvar a senha? [{a}s{f}/{a}n{f}{n}]{f} ').strip().lower()[0]
    if sal == 's':
        nome = input(f'{n}Nome do arquivo: ({amare}espaços serão substituídos por -{f}{n}){f} ').strip()
        if '  ' in nome: nome = nome.replace('  ', '-')
        if ' ' in nome: nome = nome.replace(' ', '-')
        system(f'cd senhas && touch {nome}.txt && echo {senha} >> {nome}.txt')
        print(f'{ver}Senha salva, confira a pasta "senhas"!{f}')
    try:
        per = input(f'{n}Deseja gerar outra senha? [{a}s{f}/{a}n{f}{n}]{f} ').strip().lower()[0]
    except:
        continue
    system('cls||clear')
print(f'{a}Obrigado por usar meu script, não se esqueça de avalia-lo e até mais :){f}')
