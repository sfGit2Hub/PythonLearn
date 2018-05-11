import sys
import os
from fpdf import FPDF
from PIL import Image


def make(type, name):
    if (type == "-p"):
        cover = Image.open(name)
        width, height = cover.size
        pdf = FPDF(unit="pt", format=[width, height])
        pdf.add_page()
        pdf.image(name, 0, 0)
        pdf.output(name[:-4] + ".pdf", "F")
    elif (type == "-f"):
        listpic = os.listdir(name)
        cover = Image.open(name + "/" + listpic[0])
        cover = cover.convert('1')
        width, height = cover.size
        pdf = FPDF(unit="pt", format=[width, height])

        for page in listpic:
            pdf.add_page()
            pdf.image(name + "/" + page, 0, 0)

        pdf.output(name + ".pdf", "F")

    else:
        exit()


if __name__ == '__main__':
    make(str(sys.argv[1]), str(sys.argv[2]))
