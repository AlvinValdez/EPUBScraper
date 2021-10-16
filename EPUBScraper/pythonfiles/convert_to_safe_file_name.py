import re

def convert_to_file_name(filename):
    newFileName = re.sub("[#\s<$+%>!'`\"&*|{}?/:@\\\]","-",filename)
    cleanedFileName = re.sub("\-{2,}","-",newFileName)
    return cleanedFileName
