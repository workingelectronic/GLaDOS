import urllib3

def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

file = open("/home/dell/PycharmProjects/IoT/Luces/State.txt", "r")
text = file.readlines(1)
unique_code = extract_unique_code(text)
print(text)

if state is "Encender":
    if room  == "baño":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/on')
        print(r.data)
    elif room  == "cocina":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/on')
        print(r.data)
    elif room == "salon":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/on')
        print(r.data)
    elif room == "cuarto":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/on')
        print(r.data)
    elif room == "todo":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/on')
        print(r.data)

elif state is "Apagar":
    if room  == "baño":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/off')
        print(r.data)
    elif room  == "cocina":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/off')
        print(r.data)
    elif room == "salon":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/off')
        print(r.data)
    elif room == "cuarto":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/off')
        print(r.data)
    elif room == "todo":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.31.125/off')
        print(r.data)

'''
-------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------
'''


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

file = open("/home/dell/PycharmProjects/IoT/Luces/State.txt", "w")
file.write(result)
file.close()
