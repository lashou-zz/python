def readFile(path):
        f = open(path);
        line = f.readline();
        while line:
            print line;
            line = f.readline();
        f.close();
readFile('readFile.py');
