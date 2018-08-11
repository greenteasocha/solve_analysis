def main():
    path = "roux"
    out = path + ".rep"
    with open(path, "r") as f:
        seq = f.read()

    old = ["R2'", "L2'", "U2'", "D2'", "F2'", "B2'"]
    new = ["R2", "L2", "U2", "D2", "F2", "B2"]

    for o,n in zip(old,new):
        seq = seq.replace(o, n)

    with open(out, "w") as f:
        f.write(seq)

if __name__ == "__main__":
    main()