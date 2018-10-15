import re;

import xlsxwriter

from PiLibraries import Constants
from PiLibraries.SheetWriter import SheetWriter


class PIworkbookLog():

    def __init__(self, filename=None):
        if filename == None:
            print('Generate xlsx file impossible');
            return;
        try:
            self.filename = re.search(Constants.regexFileName, filename).group(1);
        except AttributeError as err:
            self.filename = filename;
        self.workbook = xlsxwriter.Workbook(Constants.outputFolder + '/' + self.filename + '.xlsx')
        self.sheetErrorWarning = SheetWriter(self.workbook, 'Error&Warning', Constants.columnSheet[:6], 'A:F', 50);
        self.sheetPointNotFound = SheetWriter(self.workbook, 'PiPointNouFound', [Constants.columnSheet[6]], 'A:A');
        self.point = set();

    def saveFile(self):
        self.workbook.close();

    def addErrorWarning(self, line):
        result = re.search(Constants.regexWithAF, line);
        if result != None:
            self.generateRowAF(result);
        else:
            result = re.search(Constants.regexGenerics, line);
            if result == None:
                return;
            self.sheetErrorWarning.createRow(list(result.groups()), True)

    def generateRowAF(self, res):
        listRes = list(res.groups());
        pathAn = listRes.pop();
        self.sheetErrorWarning.createRow(listRes, False)
        result = re.search(Constants.regexForPath, pathAn);
        self.sheetErrorWarning.createRow(list(result.groups()), True, 4);

    def addPiPointNotFound(self, line):
        res = re.search(Constants.regexPiPoint, line);
        if res.group(1) not in self.point:
            self.sheetPointNotFound.createRow(res.group(1), True, 0)
            self.point.add(res.group(1));
