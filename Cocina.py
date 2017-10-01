import urllib3

url = "http://192.168.31.125"

file = open("onoff.txt", "r")
answer = file.read()
print(answer)


def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


if answer == "on":
    http = urllib3.PoolManager()
    r = http.request('GET', url + '/on')
    unique_code = extract_unique_code(r.data)
    print(r.data)
elif answer == "off":
    http = urllib3.PoolManager()
    r = http.request('GET', url + '/off')
    unique_code = extract_unique_code(r.data)
    print(r.data)
elif answer == "toggle":
    http = urllib3.PoolManager()
    r = http.request('GET', url + '/toggle')
    unique_code = extract_unique_code(r.data)
    print(r.data)
else:
    print("algo fallo")


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
