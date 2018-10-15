# Pi Logger Analizer

![CI status](https://img.shields.io/badge/python-3.0-orange.svg) ![](https://img.shields.io/badge/Version-1.0-green.svg)

Is a little Python Script for Analize Osisoft Pi Log file.  Get in input a file.txt e search Error/Warning/Pi Point not Found.
After Analyzing, it create a xlsx file with the report.

## Installation

### Requirements

* Python 3.3 and up
* pip
### Install
* `$ pip install XlsxWriter` 
* or from root project `$ pip install -r requirements.txt`





## How it use?
From command-line:

    python PiLoggerAnalizer.py -d ./Example
    
##### Command-Line options:
* -d, --directory = To specific Input directory, when there are the file log.txt
* -r, --rename = For rename the export file with another naming convention

NB.Default it analize File individually



## Contribute
All contributions are always welcome


## Powered by
    Antonino Di Carlo
