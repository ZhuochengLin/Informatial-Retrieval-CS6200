import os
import re
import json

def file_parser():
    # read all file names from the directory
    file_name = os.listdir("./ap89_collection/")
    file_name = ["./ap89_collection/" + i for i in file_name]

    # needed objects
    files = {}
    file = list()
    add_file_flag = 0

    txt = list()
    txt_item = list()
    txt_flag = 0

    # read each file
    for f in file_name:
        with open(f, "r") as f:
            data = f.readlines()
            # scan each line, identify doc start and end
            for line in data:
                line = line.strip()
                # file end
                if re.search("</DOC>", line):
                    add_file_flag = 0
                    files[data_id] = ' '.join(file)
                    file = list()
                # add lines to file
                if add_file_flag == 1:
                    # id
                    if re.search("</DOCNO>", line):
                        data_id = re.sub("(<DOCNO> )|( </DOCNO>)", "", line)
                    # read text chunk
                    # text end
                    if re.search("</TEXT>", line):
                        txt_flag = 0
                    if txt_flag == 1:
                        file.append(line)
                    # text start
                    if re.search("<TEXT>", line):
                        if re.search("[A-Z|a-z]*[a-z]", line):
                            file.append(line[6:])
                        txt_flag = 1
                # file start
                if re.search("<DOC>", line):
                    add_file_flag = 1
    return files


def write_file(files):
    with open("./parsed_file.json", "w") as f:
        json.dump(files, f)


files = file_parser()
write_file(files)
