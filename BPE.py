from collections import defaultdict
import re

def BPE(lines):
    conv = {}
    new_symbol = "ACGHIJKNOPQTVWXYZ"
    for i in range(4,1000):
        dic = bigram(lines)
        max_k = max(dic, key=dic.get) # most frequent pair
        if dic[max_k] <= 3:
            break
        for j, l in enumerate(lines):
            d = re.match(max_k + " ", l)
            if d:
                lines[j] = lines[j].replace(max_k + " ", str(i) + " ", 1)
            lines[j] = lines[j].replace(" " + max_k+" ", " " + str(i)+" ") # replace
        for k in max_k.split(" "):
            if k in conv.keys():
                max_k = max_k.replace(k, conv[k])
        conv[str(i)] = max_k
    print(conv)
    for k, v in sorted(conv.items(), key=lambda x: -len(x[1])):
        print(str(k) + ": " + str(v))
    with open("seq1.bpe", "w") as f:
        f.write("".join(lines))

def bigram(lines):
    dic = defaultdict(int)
    for l in lines:
        if len(l) <= 10:
            continue
        turns = l.split(" ")
        for r, s in zip(turns[:-1], turns[1:]):
            if "\n" not in [r,s]:
                dic[r + " " + s] += 1
    return dic

def main():
    path = "roux.out"

    with open(path, "r") as f:
        lines = f.readlines()

    BPE(lines)

if __name__ == "__main__":
    main()