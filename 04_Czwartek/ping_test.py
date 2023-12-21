import dumper
import subprocess

command = ["ping", "-c", "4", "150.254.65.8"]
ret_code = subprocess.run(command, capture_output=True)
print(dumper.dump(ret_code))
print(ret_code.stdout.decode())
print(ret_code.returncode)