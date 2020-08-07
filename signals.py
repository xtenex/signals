#!/usr/bin/env python3
#Esto es solo un ejercicio para entender como se pueden atrapar las senales que se ilustran en
# el manual 7 de linux
import signal

def main():
    signal.signal(signal.SIGINT, test)
    # se llama a signal, y el primer argumento es el tipo de senal que se muestran en el man 7 signal
    # el segundo argumento manda llamar la funcion test que es lo que se ejecutara en lugar del Ctrl + C
    while True:
        continue

def test(sig, frm):
    print(f"signal: {sig}\notra cosa: {frm}")
    print("esta es la funcion")

if __name__ == '__main__':
    main()
