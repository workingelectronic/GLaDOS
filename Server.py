import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://192.168.31.125/toggle')
print(r.data)

def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

unique_code = extract_unique_code(r.data)

print(unique_code)

if unique_code == b'on':
    result = "Encendido"
    print("Encendido")

elif unique_code == b'off':
    result = "Apagado"
    print("Apagado")
else:
    print("vuelve a mirar")

file = open("State.txt", "w")
file.write(result)
file.close()
