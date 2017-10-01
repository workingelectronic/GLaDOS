import subprocess

# Quizas seria mejor hacerlo con un for y un vector para las habitaciones
subprocess.check_call(["python3", "Baño.py"])
subprocess.check_call(["python3", "Cocina.py"])
subprocess.check_call(["python3", "Salón.py"])
subprocess.check_call(["python3", "Cuarto.py"])
subprocess.check_call(["python3", "Pasillo.py"])