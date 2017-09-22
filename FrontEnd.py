from tkinter import *
from BackEnd import DatabaseConnector


class MainWindow:
    "This class defines the front end for our database program"

    def __init__(self):
        self.initGUI()
        self.buildGUI()
        self.startBackEnd()
        self.startGUI()

    def initGUI(self):               
        self.root = Tk()
        self.root.wm_title("Database Manager")
        self.topFrame = Frame(self.root)
        self.bottomFrame = Frame(self.root)
        self.topFrame.pack(side = TOP)
        self.bottomFrame.pack(side = BOTTOM)

        self.fnameVariable = StringVar()
        self.txt_Fname = Entry(self.topFrame, textvariable = self.fnameVariable)
        
        self.lnameVariable = StringVar()
        self.txt_Lname = Entry(self.topFrame, textvariable = self.lnameVariable)

        self.txt_IDNumber = Entry(self.topFrame)

        self.gpaVariable = StringVar()
        self.txt_GPA = Entry(self.topFrame, textvariable = self.gpaVariable)
        
        self.btn_Insert = Button(self.bottomFrame,text="Insert", command = self.insertEvent)
        self.btn_Update = Button(self.bottomFrame,text="Update", command = self.updateEvent)
        self.btn_Remove = Button(self.bottomFrame,text="Remove", command = self.removeEvent)
        self.btn_Get = Button(self.bottomFrame,text="Get", command = self.getEvent)

    def buildGUI(self):
        self.btn_Insert.pack(side = LEFT)
        self.btn_Update.pack(side = LEFT)
        self.btn_Remove.pack(side = LEFT)
        self.btn_Get.pack(side = LEFT)

        self.txt_Fname.pack(side = LEFT)
        self.txt_Lname.pack(side = LEFT)
        self.txt_IDNumber.pack(side = LEFT)
        self.txt_GPA.pack(side = LEFT)

    def startGUI(self):
        self.root.mainloop()

    #insert new row with all 4 fields
    def insertEvent(self):
        fname = self.txt_Fname.get()
        lname = self.txt_Lname.get()
        idNumber = self.txt_IDNumber.get()
        gpa = self.getGPA()
        self.backEnd.insert(fname,lname,idNumber,gpa)

    #update based on ID
    def updateEvent(self):
        fname = self.txt_Fname.get()
        lname = self.txt_Lname.get()
        idNumber = self.txt_IDNumber.get()
        gpa = self.getGPA()
        self.backEnd.update(fname,lname,idNumber,gpa)

    #remove based on ID
    def removeEvent(self):
        idNumber = self.txt_IDNumber.get()
        self.backEnd.remove(idNumber)
        
    #get based on ID
    def getEvent(self):
        idNumber = self.txt_IDNumber.get()
        self.backEnd.get(idNumber)

    def startBackEnd(self):
        self.backEnd = DatabaseConnector("www.soulsoftware.ca","pythonuser","python2017","cprg104")

    def getGPA(self):
        try:
            gpa = float(self.txt_GPA.get())
            if(gpa >= 0 and gpa <= 4):
                return str(gpa)
            else:
                print("Invalid ! GPA must be between 0 and 4 !")
                self.gpaVariable.set(" ")
        except Exception as arg:
            print("Invalid GPA ! Please enter a new value",arg)
            self.gpaVariable.set(" ")

