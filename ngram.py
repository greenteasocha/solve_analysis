from collections import defaultdict
from argparse import ArgumentParser

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
    parser = ArgumentParser()
    parser.add_argument('--path', default="data/CFOP.lin", type=str, help='input file')
    parser.add_argument('--threshold', default=20, type=int, help='lower frequency')
    parser.add_argument('--n', default="4", type=int, help='n gram')
    args = parser.parse_args()

    with open(args.path, "r") as f:
        lines = f.readlines()

    if args.n == 2:
        dic = bigram(lines)
    elif args.n == 3:
        dic = trigram(lines)
    elif args.n == 4:
        dic = four_gram(lines)
    else:
        raise Exception

    for k, v in sorted(dic.items(), key=lambda x: -x[1]):
        if v >= args.threshold:
            print(str(k) + ": " + str(v))

if __name__ == "__main__":
    main()