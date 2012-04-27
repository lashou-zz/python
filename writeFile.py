def writeFile(content, file):
    f = open(file, 'r+');
    f.write(content);
    f.close();
writeFile("hello world", "temp/files");
