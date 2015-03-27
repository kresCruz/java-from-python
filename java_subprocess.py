from subprocess import Popen, STDOUT, PIPE, TimeoutExpired


class PyJavaRun(object):
	"""
	PyJavaRun is a class that run a java program through subprocess class
	"""
	_exec = 'java'
	
	def __init__(self, name=None, timeout=None, params=[]):
		if not type(name) == str:
			raise TypeError(
				'The `name` must be a str. Got %s.' %
				type(params).__name__
			)

		if not isinstance(params, list):
			raise TypeError(
				'The `params` must be a list. Got %s.' %
				type(params).__name__
			)

		self._name = name
		self._options = ['-jar']
		self._params = params
		self._timeout = timeout
		self.run()

	def command_args(self):
		options = ''.join(self._options)
		command = [self._exec, options, self._name] + self._params
		return command

	def run(self, stdout=PIPE, stderr=STDOUT):
		"""
		Run command through subprocess.communicate() method.
		"""
		args = self.command_args()
		process = Popen(args, stdout=stdout, stderr=stderr)

		try:
			self._output, self._errors = process.communicate(timeout=self._timeout)
			self._returncode = process.returncode
			process.kill()
		except TimeoutExpired:
			raise
		finally:
			process.kill()
		
	@property
	def returncode(self):
		return self._returncode

	@property
	def errors(self):
		return self._errors

	@property
	def output(self):
		return self._output
