#coding=utf-8
import re
import sys

stringTable = open(sys.argv[1]).read().split('\n')

buffer = ''

stringTablemod = open(sys.argv[1] + '.new', 'w')

mapStr = open(sys.argv[2]).read().strip().split('\n')

mapTable = {}

for line in mapStr:
    line = line.split('\t')
    mapTable[line[0]] = line[1]


for line in stringTable:
    if line.find('<Chinesesimp>') != -1:
        labeledContentmatch = re.search('<Chinesesimp>(.+)</Chinesesimp>', line)
        labeledContent = labeledContentmatch.group(1)
        possibleAlphabetical = re.findall('\w+', labeledContent)
        if possibleAlphabetical:
            for alphabeticalLiteral in possibleAlphabetical:
                for i in mapTable:
                    if i == alphabeticalLiteral:
                        line = line.replace(i, mapTable[i])
        #quotation mark pairing

    buffer += (line + '\n')

stringTablemod.write(buffer)
stringTablemod.close()