from collections import defaultdict

def bigram(lines):
    dic = defaultdict(int)
    for l in lines:
        if len(l) <= 10:
            continue
        turns = l.split(" ")
        for r, s in zip(turns[:-1], turns[1:]):
            if "\n" not in [r,s]:
                dic[r+s] += 1
    return dic


def trigram(lines):
    dic = defaultdict(int)
    for l in lines:
        if len(l) <= 10:
            continue
        turns = l.split(" ")
        for r, s, t in zip(turns[:-2], turns[1:-1], turns[2:]):
            if t not in ["x","y","z"]:
                dic[r+s+t] += 1
    return dic

def four_gram(lines):
    dic = defaultdict(int)
    for l in lines:
        if len(l) <= 10:
            continue
        turns = l.split(" ")
        for r, s, t, u in zip(turns[:-3], turns[1:-2], turns[2:-1], turns[3:]):
            if u not in ["x","y","z"]:
                dic[r+s+t+u] += 1
    return dic

def main():
    path = "seq1.out"
    threshold = 20
    n = 2

    with open(path, "r") as f:
        lines = f.readlines()

    if n == 2:
        dic = bigram(lines)
    elif n == 3:
        dic = trigram(lines)
    elif n == 4:
        dic = four_gram(lines)
    else:
        raise Exception

    for k, v in sorted(dic.items(), key=lambda x: -x[1]):
        if v >= threshold:
            print(str(k) + ": " + str(v))

if __name__ == "__main__":
    main()