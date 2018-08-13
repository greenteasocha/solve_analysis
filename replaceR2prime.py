from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('--path', default="CFOP.txt", type=str, nargs="+", help='input file')
    args = parser.parse_args()

    with open(args.path, "r") as f:
        seq = f.read()

    old = ["R2'", "L2'", "U2'", "D2'", "F2'", "B2'"]
    new = ["R2", "L2", "U2", "D2", "F2", "B2"]

    for o,n in zip(old,new):
        seq = seq.replace(o, n)

    with open(args.path, "w") as f:
        f.write(seq)

if __name__ == "__main__":
    main()