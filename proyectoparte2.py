def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario   #pasar a numero binario

def lfsr(seed, taps):
    import time
    sr, xor = seed, 0
    while 1:
        for t in taps:
            xor += int(sr[t-1])
        if xor%2 == 0.0:
            xor = 0
        else:
            xor = 1
        print (xor)
        print
        time.sleep(0.75)
        sr, xor = str(xor) + sr[:-1], 0
        print (sr)
        print
        time.sleep(0.75) #LFSR para generar secuencia de numeros que hagan encriptacion y desencriptacion
          



