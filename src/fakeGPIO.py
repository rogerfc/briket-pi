import yaml

BOARD	= None
IN		= None
OUT		= None

inputfile = 'fakeniput.yaml'

def setmode(dummy):
	pass

def setup(port, dummy):
	pass
	
def input(port):
	return yaml.safe_load(open('ioconfig.yaml'))[port]
	# return True
	
def output(port, value = True):
	print 'setting output port %s to %s' % (port, value)
	
