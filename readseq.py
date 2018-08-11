import re
def open_seq(path):
    """

    :param path: path for raw solve reconstruction
    :return: list of executions. Each solve divided by empty element
    """
    with open(path, "r") as f:
        seq = f.readlines()
    return seq

class Reconstruction():
    def __init__(self, lines):
        """

        :param lines: list of sequences
        """
        self.org = lines
        self.sequence = []

    def divide_solves(self):
        """

        :return: solves as str. Each line means each solve
        """
        solve = []
        all = []
        for l in self.org:
            solve.append(l)
            if len(l) <= 1:
                s = self.makeline(solve)
                solve = []
                all.append(s)
        s = self.makeline(solve)
        all.append(s)                     # for last solve
        return all

    def makeline(self, solve):
        """

        :param solve: list of execution like [[U R U' R' //sexy], [R' F R F' //sledge]]
        :return: U R U' R' R' F R F'
        """
        sequence = []
        pattern = "\((.)*\)(\s)*."
        for l in solve:
            execution = l.split("//")[0]
            d = re.search(pattern, execution)
            if d:
                d1 = d.group(0)
                d2 = self.processing_repeat(d1)
                execution = execution.replace(d1,d2)
            sequence.append(execution)
        s = "".join(sequence)
        return s

    def processing_repeat(self,s):
        """
        :param s: (U R U' R')3
        :return: U R U' R' U R U' R' U R U' R'
        """
        exec = s.split(")")[0][1:]
        repeat = s[-1] # like 3
        if not re.match("\d", repeat): # for pattern like (U' D) F: not exist the number of repeat
            return exec + " " + repeat

        return ((exec + " " ) * int(repeat))[:-1]

def main():
    path = "roux.rep"
    out = path[:-3]+"out"
    seq = open_seq(path)
    r = Reconstruction(seq)
    s = r.divide_solves()
    with open(out, "w") as f:
        f.write("".join(s).replace("  ", " ")) # processing double space produced by processing_repeat

if __name__ == "__main__":
    main()