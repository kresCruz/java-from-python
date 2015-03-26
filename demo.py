from java_subprocess import PyJavaRun

run = PyJavaRun('DemoJava.jar', params=['foo'])

print(run.output)
print(run.errors)