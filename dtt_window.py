import scipy.stats as stats
import itertools
import numpy as np
from sys import argv
script, infile = argv




def summary_tetra(seq):
    tetra_dict = {}
    for i in itertools.product('ACGT', repeat = 4):
        tetra = ''.join(i)
        tetra_dict[tetra] = 0
    start = 0
    window = 4
    step_size = 1
    while True:
        if window < len(seq) + 1:
            tetra = seq[start: window]
            tetra_dict[tetra] += 1
            start += step_size
            window += step_size
        else:
            break
    return tetra_dict

def frequency(dict):
    list = []
    sum = 0
    for i in dict:
        sum += dict[i]
    for i in dict:
        fre = dict[i]/sum
        list.append(fre)
    dict = []
    return list

with open(infile) as file1:
    lines1 = file1.readlines()
sequence = ''
for line in lines1:
     if not line.startswith('>'):
         sequence += line.replace("\n", '')   #读取序列
sequence = sequence[len(sequence)-5000:len(sequence)] + sequence + sequence[0:5000]
lista = frequency(summary_tetra(sequence))
stda = np.std(lista, ddof=1)
meana = np.mean(lista)
for i in range(len(lista)):
    lista[i] = (lista[i]-meana)/stda
fstart = 0
fwindow = 10000
fstep_size = 1000
while True:
    if fwindow < len(sequence) + 1:
        fseq = sequence[fstart: fwindow]
        listn = frequency(summary_tetra(fseq))
        stdn = np.std(listn, ddof=1)
        meann = np.mean(listn)
        for i in range(len(listn)):
            listn[i] = (listn[i]-meann)/stdn
        pi = stats.pearsonr(lista, listn)
        print("%8d\t%.3f\t%.3f" % (fstart, pi[0], pi[1]))
        fstart += fstep_size
        fwindow += fstep_size
    else:
        break
