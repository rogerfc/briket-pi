#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import yaml

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

class Briket(object):

	def __init__(self, ioconfig):
		self.config			= ioconfig
		self.porta			= Component(self.config['porta'])
		self.pisto			= Component(self.config['pisto'])
		self.premsa			= Component(self.config['premsa'])
		self.alimentador	= Component(self.config['alimentador'])

	def __repr__(self):
		return '<Briketadora Pi>'
		
	def __str__(self):
		return 'Briket'

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
	
	def __init__(self, input_config):
		self.config				= input_config
		self.nom 				= input_config['nom']
		self.endswitch_obert	= input_config['port_finaldelinia_obert']
		self.endswitch_tancat	= input_config['port_finaldelinia_tancat']
		self.actuador_obrir		= input_config['port_actuador_obrir']
		self.actuador_tancar	= input_config['port_actuador_tancar']

		# definim endswitches com a IN
		GPIO.setup(self.endswitch_obert, GPIO.IN)
		GPIO.setup(self.endswitch_tancat, GPIO.IN)
		# # definim actuadors com a OUT
		GPIO.setup(self.actuador_obrir, GPIO.OUT)
		GPIO.setup(self.actuador_tancar, GPIO.OUT)
		# # No se si és necessari, pero per si de cas resettejem la sortida
		GPIO.output(self.actuador_obrir, False)
		GPIO.output(self.actuador_tancar, False)

	def __repr__(self):
		return '<Briket Component: %s>' % self.nom

	def __str__(self):
		return '%s' % self.nom

	def obrir(self):
		pass
	
	def tancar(self):
		pass
		
	@property
	def obert(self):
		return True if GPIO.input(self.endswitch_obert) else False
		# return True if self.endswitch_obert else False

	@property
	def tancat(self):
		return True if GPIO.input(self.endswitch_tancat) else False
		# return True if self.endswitch_tancat else False
		
	@property
	def estat(self):
		if self.obert:
			if not self.tancat:
				return 'Obert'
			return 'Obert i Tancat'
		elif self.tancat:
			return 'Tancat'
		else:
			return 'Ni Obert ni Tancat'
		
def main():
	ioconfig = yaml.safe_load(open('ioconfig.yaml'))
	brik = Briket(ioconfig)

	print brik
	print brik.config
	print brik.pisto
	print brik.premsa.estat

if __name__ == '__main__':
	main()