# Vogliamo creare uno script che prende in input un file di log di PI, lo analizza salvando su spreadsheet diversi:
# 1- Errori e Warning
# 2- Pi Point not found
#
# operazioni da console: -i indicare la cartella di input
#                       -d specifica che è una cartella
#                          di default prende un file
#                       -n nome del fileoutput
#
import getopt
import os
import re
import sys
import time

from PiLibraries import Constants
from PiLibraries.PiLogAnalizer import PiLogAnalizer


def openMenuOperation():
    inputClient = None;
    try:
        inputClient = int(
            input('How to rename files:\n1-Original file name\n2-Input by keyboard\n'));
        if inputClient == 1:
            holdDefaultName();
        elif inputClient == 2:
            renameExport()
    except ValueError:
        print('You can use just the displayed command')


def holdDefaultName():
    for file in os.listdir(Constants.inputFolder):
        print('Analyzing %s...' % file, end="");
        pi = PiLogAnalizer(file);
        pi.analizeFile();
        print('Done!');
    print();


def getNewName(newName, file):
    part2 = re.search('-(.*)', file);
    if part2 is None:
        print('Error, separator character  \'-\' not found in %s, use default name' % file);
        return file;
    else:
        return newName + '-' + part2.group(1);


def renameExport():
    print('Example filename: XXXXXXXX-yyyyyyy ( X = filename, y=otherCharacter');
    newName = input('New name:\n')
    for file in os.listdir(Constants.inputFolder):
        print('Analyzing %s...' % file);
        newNameFile = getNewName(newName, file);
        pi = PiLogAnalizer(file, newNameFile);
        pi.analizeFile();
        print('Done!');


def analizeName(name):
    result = re.search(Constants.regexName, name);
    if result.group(1) is not None:
        Constants.inputFolder = result.group(1);
    return result.group(2);


argv = sys.argv[1:]

opts, args = getopt.getopt(argv, "dr:", ["directory", "rename="])

optsDict = dict((x, y) for x, y in opts);

if len(args) == 0:
    print('No file selected');
    sys.exit()


if '-d' in optsDict:
    if len(args) > 1:
        print('Warning: You can analize just a folder\n')
    print('Analyzing Folder: \'%s\'...' % args[0])
    Constants.inputFolder = args[0];
    openMenuOperation()
else:
    for fileAn in args:
        nameFile = analizeName(fileAn);
        print('Analyzing %s...' % nameFile, end="");
        pi = PiLogAnalizer(nameFile, optsDict.get('-r'));
        pi.analizeFile();
        print('...Done!')


print('Finished')
time.sleep(2);
