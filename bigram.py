from collections import defaultdict

def main():
    path = "seq1.out"
    with open(path, "r") as f:
        lines = f.readlines()

    dic = defaultdict(int)
    for l in lines:
        if len(l) <= 10:
            continue
        turns = l.split(" ")
        for r, s in zip(turns[:-1], turns[1:]):
            if s not in ["x","y","z"]:
                dic[r+s] += 1

    print(dic)
if __name__ == "__main__":
    main()