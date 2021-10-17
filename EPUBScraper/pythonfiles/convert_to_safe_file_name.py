import re

def convert_to_file_name(filename):
    """
    Takes a string that will be used as a filename and converts to a safe filename.
    :param filename:
    :return cleanedFileName:
    """
    newFileName = re.sub("[#\s<$+%>!'`\"&*|{}?/:@\\\]","-",filename)
    cleanedFileName = re.sub("\-{2,}","-",newFileName)
    return cleanedFileName
