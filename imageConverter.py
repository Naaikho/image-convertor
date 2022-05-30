import traceback
from PIL import Image



class ImageConvertor:

    def __init__(self, file, ext, outDir="", outName=""):
        file = r"".join(file.split('"'))
        if outName == "":
            outName = self.nameOut(file)
        outDir = self.directoryOut(file) if outDir == "" else self.fileOut(outDir)
        Image.open(file).save("{}\\{}.{}".format(outDir,outName,ext))

    def nameOut(self, filePath)->str:
        filePath = ".".join(filePath.replace("/", ",").replace("\\", ",").split(",")[-1].split(".")[0:-1])
        return filePath

    def fileOut(self, dirPath)->str:
        dirPath = r"\\".join(dirPath.replace("/", ",").replace("\\", ",").split(","))
        return dirPath

    def directoryOut(self, filePath)->str:
        dirOut = r"\\".join(filePath.replace("/", ",").replace("\\", ",").split(",")[:-1])
        return dirOut



if __name__ == "__main__":
    while 1:
        try:
            ImageConvertor(input("Image: "), input("Extention: ."), input("Directory [if empty same as file]: "), input("Name [if empty same as file]: "))
            print("Done")
        except Exception:
            print(traceback.format_exc())