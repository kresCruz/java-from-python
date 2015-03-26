from subprocess import Popen, STDOUT, PIPE


class PJavaRun(object):
	"""
	PyJavaRun is a class that run a java program through subprocess class
	"""
	_exe = 'java'
	_options = {}
	
	def __init__(self, name=None):
		self._name = name
		self._options = ['-jar']
		self.run()

	def command_args(self):
		options = ''.join(self._options)
		command = [self._exe, options, self._name]
		return command

	def run(self, stdout=PIPE, stderr=STDOUT):
		args = self.command_args()
		process = Popen(args, stdout=stdout, stderr=stderr)
		self._output, self._errors = process.communicate()
		process.kill()
