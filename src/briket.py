#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import yaml

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

class Briket(object):

	def __init__(self, ioconfig):
		self.porta			= Component('Porta', 		ioconfig['porta']['ino'], ioconfig['porta']['int'], ioconfig['porta']['outo'], ioconfig['porta']['outt'])
		self.pisto			= Component('Pistó', 		ioconfig['pisto']['ino'], ioconfig['pisto']['int'], ioconfig['pisto']['outo'], ioconfig['pisto']['outt'])
		self.premsa			= Component('Premsa', 		ioconfig['premsa']['ino'], ioconfig['premsa']['int'], ioconfig['premsa']['outo'], ioconfig['premsa']['outt'])
		self.alimentador	= Component('Alimentador',	ioconfig['alimentador']['ino'], ioconfig['alimentador']['int'], ioconfig['alimentador']['outo'], ioconfig['alimentador']['outt'])

	def baixar_porta():
		self.porta.tancar()
		
	def pujar_porta():
		self.porta.obrir()
		
	def tirar_enrere():
		self.pisto.obrir()
		
	def mini_tirar_enrere():
		self.pisto.obrir()
		
	def empenyer_briketa():
		self.pisto.tancar()
		
	def empenyer_3_briketes():
		self.pisto.tancar()
	
	def premsar_briketa():
		self.premsa.tancar()
		
	def tirar_virutes():
		self.alimentador.obrir()
		
	def mas_madera():
		self.alimentador.obrir()
		
	def main():
		pass
	
	
class Component(object):
	
	def __init__(self, nom, input_obert, input_tancat, output_obrir, output_tancar):
		self.nom 				= nom
		self.endswitch_obert	= input_obert
		self.endswitch_tancat	= input_tancat
		self.actuador_obrir		= ouput_obrir
		self.actuador_tancar	= ouput_tancar

		# definim endswitches com a IN
		GPIO.setup(self.endswitch_obert, GPIO.IN)
		GPIO.setup(self.endswitch_tancat, GPIO.IN)
		# definim actuadors com a OUT
		GPIO.setup(self.actuador_obrir, GPIO.OUT)
		GPIO.setup(self.actuador_tancar, GPIO.OUT)
		# No se si és necessari, pero per si de cas resettejem la sortida
		GPIO.output(self.actuador_obrir, False)
		GPIO.output(self.actuador_tancar, False)

	def obrir(self):
		pass
	
	def tancar(self):
		pass
		
	@property
	def obert(self):
		return True if GPIO.input(self.endswitch_obert) else False

	@property
	def tancat(self):
		return True if GPIO.input(self.endswitch_tancat) else False
		
def main():
	ioconfig = yaml.safe_load(open('src/ioconfig.yaml'))

if __name__ == '__main__':
	main()