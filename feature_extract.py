from argparse import ArgumentParser
import json

def extract_feature(line, method):
    turns = ["U", "D", "R", "L", "B", "F", "M", "S", "E"]
    feature = [line.count(i) for i in turns]
    feature = feature + [sum(feature)]
    if method =="CFOP":
        label = 1
    elif method == "Roux":
        label = 2
    else:
        raise Exception
    d = {"label":label, "feature":feature}
    return d

def main():
    parser = ArgumentParser()
    parser.add_argument('--file', default="data/CFOP.lin", type=str, help='input file')
    parser.add_argument('--out', default="data/CFOP.json", type=str, help='output file')
    parser.add_argument('--method', default="CFOP", type=str, choices=["CFOP", "Roux"])
    args = parser.parse_args()

    with open(args.file, "r") as f:
        lines = f.readlines()

    features = []
    for line in lines:
        features.append(extract_feature(line, args.method))
    output = {"solves":features}
    print(output)
    with open(args.out, "w") as f:
        json.dump(output, f)


if __name__ == "__main__":
    main()