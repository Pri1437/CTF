def convert(value, base):
    char = chr(int(value, base))
    return char

def hxTostr(hseq):
    i = 0
    cseq = []
    while i < len(hseq)-1:
        hx = hseq[i:i+2]
        cseq.append(chr(int(hx, 16)))
        i=i+2
    return cseq

#print(type(input()))
while True:
    seq = input('enter seq\n').split()
    if seq[0] == 'exit':
        quit()

    base = int(input('enter base\n'))
    cseq = []
    if base != 16:
        cseq = [convert(i,base) for i in seq]
    else:
        cseq = hxTostr(seq[0])
    string = ""
    for c in cseq:
        string+=c
    print(string)
