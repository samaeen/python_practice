import pyttsx

# function for saying out loud
def saySomething():
	engine = pyttsx.init()
	engine.say('aumi banglai gan gai .aumi banglai gan gai..aumi amar abege chirodin ei banglai gan gai')
	#engine.say('Sally sells seashells by the seashore.')
	#engine.say('The quick brown fox jumped over the lazy dog.')
	engine.runAndWait()

#look For Event
def lookforevent():
	def onStart(name):
		print ('starting', name)
	def onWord(name, location, length):
		print ('word', name, location, length)
	def onEnd(name, completed):
		print ('finishing', name, completed)
	engine = pyttsx.init()
	engine.connect('started-utterance', onStart)
	engine.connect('started-word', onWord)
	engine.connect('finished-utterance', onEnd)
	engine.say('The quick brown fox jumped over the lazy dog.Banglai gan gai')
	engine.runAndWait()

saySomething()
