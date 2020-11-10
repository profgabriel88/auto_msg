'''
Automação de mensagens simples
Autor: Gabriel Dai
2020

Manda a mesma mensagem repetidamente em intervalos de tempo constantes.
'''

from pynput.keyboard import Key
from pynput.keyboard import Controller as kControl
from pynput.mouse import Controller as mControl
from time import sleep

kb = kControl()
mouse = mControl()

# intervalo entre as mensagens
tempo = 10

sleep(tempo)

# captura a posição atual do mouse
posAtual = mouse.position
posAnterior = posAtual

while True:

	if posAtual == posAnterior:
		
		kb.type("Mensagem automática: A aula começará em breve, aguarde.")
		
		kb.press(Key.enter)
		kb.release(Key.enter)
		
		sleep(tempo)
		
		posAtual = mouse.position
		
	else:
		
		break
