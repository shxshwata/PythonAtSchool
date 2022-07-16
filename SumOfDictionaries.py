dA = {'A': 23, 'B': 11, 'C': 6}
dB = {'D': 10, 'C': 12, 'A': 4}

for key in dB:
   if key in dA:
      dB[key] = dB[key] + dA[key]
   else:
      pass
print("Sum= ",dB)

dC = {'A': 23, 'B': 11, 'C': 6}
dD = {'D': 10, 'C': 12, 'A': 4}

for key in dD:
    if key in dC:
        dD[key]=dC[key]-dD[key]
    else:
        pass
print("Difference= ",dC)
