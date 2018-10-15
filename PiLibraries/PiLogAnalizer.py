import os
import re;

from PiLibraries import Constants
from PiLibraries.PIworkbookLog import PIworkbookLog;


class PiLogAnalizer():
    errWarnList = []
    pointNotFoundList = []

    def __init__(self, file, renameFile=None):
        self.file = file;
        if renameFile is None:
            self.fileExcel = PIworkbookLog(file);
        else:
            self.fileExcel = PIworkbookLog(renameFile);


    @property
    def file(self):
        return self.__file;

    @file.setter
    def file(self, file):
        self.__file = file;

    def analizeFile(self):
        self.checkFolderOutput()
        try:
            with open(Constants.inputFolder + '/' + self.file) as fl:
                line = fl.readline();
                while line:
                    self.findErrorWarning(line);
                    self.findPiPointNotExists(line);
                    line = fl.readline();
            self.fileExcel.saveFile();
        except FileNotFoundError:
            print("%s not found" % self.file);

    def findErrorWarning(self, line):
        validReg = ".*\|(ERROR|WARN)\|.*";
        if re.match(validReg, line):
            self.fileExcel.addErrorWarning(line);
            self.errWarnList.append(line);

    def findPiPointNotExists(self, line):
        validReg = ".*PI Point not found.*";
        if re.match(validReg, line):
            self.fileExcel.addPiPointNotFound(line);
            self.pointNotFoundList.append(line);

    def checkFolderOutput(self):
        if not os.path.exists(Constants.outputFolder):
            os.makedirs(Constants.outputFolder)

    def checkTimeStampinFile(self):
        try:
            with open(Constants.inputFolder + '/' + self.file) as fl:
                line = fl.readline();
                while line:
                    res = re.search(Constants.regexTimestamp, line);
                    if res is not None:
                        return res.group(1);
                    line = fl.readline();
                return None;
        except FileNotFoundError:
            print("%s not found" % self.file);


if __name__ == '__main__':
    print('this is a libraries');
