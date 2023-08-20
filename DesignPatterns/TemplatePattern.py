
"""
Template Pattern

Behavioural Pattern

Wedding Invitation -- Template
    With blessings from....
    Bride's name
    Groom's name
    Venue
    Data & time
    Something Optional Text

DataMiner App
1. Doc files
2. CSV files
3. PDF files

DocDataMiner
    mineData
        open Doc
        extract Data from Doc

        analyze Data
        generate Report

        close Doc

CSVDataMiner
    mineData
        open CSV
        extract Data from CSV

        analyze Data 
        generate Report

        close CSV

PDFDataMiner
    mineData
        open PDF
        extract Data from PDF

        analyze Data
        generate Report

        close PDF


TemplateMethod Pattern

super class

    templateMethod
        step1
        step2
        step3
        step4
        step5

    step1
    step2
    step3
    step4
    step5

subclass(superclass)

"""
from typing import final
from abc import ABC, abstractmethod


class DataMiner(ABC):

    @final
    def mineData(self, filePath):

        file = self.openFile(filePath)
        data = self.extractData(file)
        analysis = self.analyzeData(data)
        report = self.generateReport(analysis)
        self.closeFile(file)

    @abstractmethod
    def openFile(self, filepath):
        pass

    @abstractmethod
    def extractData(self, file):
        pass

    def analyzeData(self, data):
        print("Analyzing Data")
        return "analysis"

    def generateReport(self, analysis):
        print("Generating report")
        return "report"

    @abstractmethod
    def closeFile(self, file):
        pass

class DocDataMiner(DataMiner):

    def openFile(self, filepath):
        print("Opening Doc file")
        return "Doc file"
    
    def extractData(self, file):
        print("Extracting data from Doc file")
        return "Doc Data"
    
    def closeFile(self, file):
        print("closing the Doc file")

class CSVDataMiner(DataMiner):

    def openFile(self, filepath):
        print("Opening CSV file")
        return "CSV file"
    
    def extractData(self, file):
        print("Extracting data from CSV file")
        return "CSV Data"
    
    def closeFile(self, file):
        print("closing the CSV file")

class PDFDataMiner(DataMiner):

    def openFile(self, filepath):
        print("Opening PDF file")
        return "PDF file"
    
    def extractData(self, file):
        print("Extracting data from PDF file")
        return "PDF Data"
    
    def closeFile(self, file):
        print("closing the PDF file")

if __name__ == "__main__":

    docMiner = DocDataMiner()
    docMiner.mineData("docfilepath")

    print(" ")

    pdfMiner = PDFDataMiner()
    pdfMiner.mineData("pdffilepath")
