from subprocess import Popen, STDOUT, PIPE
import json

def java_call(java_file):
	"""
	Call java program through the subprocess module,
	return 'output' and 'errors' in a dict
	"""
	process = Popen("java "+java_file, stdout=PIPE, stderr=STDOUT)
	output, errors = process.communicate()
	process.kill()
	
	data = {'output': output, 'errors': errors}
	return data

response = java_call("HelloWorld")
print(response)
