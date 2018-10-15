from enum import Enum

class PiErrorLineEnum(Enum):
    TIMESTAMP = 0;
    TYPE = 1;
    EXCEPTION = 2;
    DESCRIPTION = 3;
    AF_DB = 4;
    ELEMENT_ANALYSES = 5;