import itertools
from sys import argv
import threading
script, infile = argv

di_dict = {}
tri_dict = {}
tetra_dict = {}
threads1 = []


for i in itertools.product('ACGT', repeat = 2):
    di = ''.join(i)
    di_dict[di] = 0

for i in itertools.product('ACGT', repeat = 3):
    tri = ''.join(i)
    tri_dict[tri] = 0

for i in itertools.product('ACGT', repeat = 4):
    tetra = ''.join(i)
    tetra_dict[tetra] = 0

def summary_di(seq):
    start = 0
    window = 2
    step_size = 1
    while True:
        if window < len(seq) + 1:
            di = seq[start: window]
            di_dict[di] += 1
            start += step_size
            window += step_size
        else:
            break
    return None

def summary_tri(seq):
    start = 0
    window = 3
    step_size = 1
    while True:
        if window < len(seq) + 1:
            tri = seq[start: window]
            tri_dict[tri] += 1
            start += step_size
            window += step_size
        else:
            break
    return None

def summary_tetra(seq):
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
    return None


def frequency(dict):
    sum = 0
    for i in dict:
        sum += dict[i]
    for i in dict:
        fre = dict[i]/sum
        print("%s\t%.8f" % (i, fre))

if __name__ == '__main__':
    with open(infile) as file1:
        lines1 = file1.readlines()
    for i in range(1, len(lines1), 2):
        tmp = lines1[i].strip()
        t1 = threading.Thread(target=summary_di, args=(tmp,))
        t2 = threading.Thread(target=summary_tri, args=(tmp,))
        t3 = threading.Thread(target=summary_tetra, args=(tmp,))
        threads = [t1, t2, t3]
        for t in threads:
            t.deamon = True
            t.start()
        t.join()
        lines1[i] = None
        lines1[i-1] = None

    frequency(di_dict)
    frequency(tri_dict)
    frequency(tetra_dict)
