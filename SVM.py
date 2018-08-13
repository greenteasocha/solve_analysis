from sklearn import svm
import json
from argparse import ArgumentParser
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


def read_json(path):
    with open(path, "r") as f:
        j = json.load(f)
        x_data = []
        y_label = []
        for s in j["solves"]:
            x_data.append(s["feature"])
            y_label.append(s["label"])
            #dummy data for debug
        return x_data, y_label


def main():
    parser = ArgumentParser()
    parser.add_argument('path', default="roux.json", type=str, nargs="+", help='input file(JSON)')
    args = parser.parse_args()
    x,y = [],[]
    for path in args.path:
        tx, ty = read_json(path)
        x += tx; y += ty
        print(len(ty))
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=None)

    for s in [x, y, x_train, y_train, x_test, y_test]:
        print("data_size: ", len(s))

    clf = svm.SVC()
    clf.fit(x_train, y_train)
    pred_train = clf.predict(x_train)
    accuracy_train = accuracy_score(y_train, pred_train)
    print('Train accuracy： %.2f' % accuracy_train)
    pred_test = clf.predict(x_test)
    accuracy_test = accuracy_score(y_test, pred_test)
    print('Test accuracy' % accuracy_test)
    print(pred_test)

    test_me = [[18,2,18,12,3,0,0,0,0,53]]
    l = "CFOP" if clf.predict(test_me) == 1 else "Roux"
    print("あなたの解法は " + l)

if __name__ == '__main__':
    main()
