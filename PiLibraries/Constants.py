regexWithAF = "(.*?)\|(.*?)\|(.*?)\|(.*)\s(\\\\.*)\["
regexGenerics = "(.*?)\|(.*?)\|(.*?)\|(.*)"
regexPiPoint = "PI Point not found\s\'(.*?)[\'\n]"
regexForPath = "(\\\\\\\\.*?\\\\\w*?)(\\\\.*)";
regexTimestamp = "(\d{4}-\d{2}-\d{2})"
regexFileName = "(.*)\."
regexName = "(.*\\\\)?(.*)";

columnSheet = ['TIMESTAMP', 'TYPE(ERR/WARN)', 'EXCEPTION', 'DESCRIPTION', 'AF DATABASE', 'ELEMENT/ANALYSES',
               'Pi Point Not Found'];
inputFolder = './input'
outputFolder = './export'
