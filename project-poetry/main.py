import os

shell = os.getenv("SHELL")
if shell == "/bin/bash":
    print("Greetings bash")
else:
    print(f'HELLO {shell}')
