class SheetWriter:

    def __init__(self, workbook, nameSheet, cols=None, rangeColumn='A:A', dimCol=30):
        self.nameSheet = nameSheet;
        self.cols = cols;
        self.sheet = workbook.add_worksheet(nameSheet);
        self.bold = workbook.add_format({'bold': True})
        self.indexErrWarnRow = 1;
        self.insertHead(rangeColumn, dimCol)

    def insertHead(self, rangeColumn, dimCol):
        for index, value in enumerate(self.cols, 0):
            self.sheet.write(0, index, value, self.bold);
            self.sheet.write(0, index, value, self.bold);
        self.sheet.set_column(rangeColumn, dimCol);

    def createRow(self, res, increment=False, initIndex=0):

        if type(res) == list:
            for index, value in enumerate(res):
                self.sheet.write(self.indexErrWarnRow, index + initIndex, value);
        elif type(res) == str:
            self.sheet.write(self.indexErrWarnRow, initIndex, res);

        if increment:
            self.indexErrWarnRow += 1;
