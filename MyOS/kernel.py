
global RAM
class OS:
    def __init__(self):
        print("Initializing OS...")
        self.boot()
        print("OS Booted!")
        print("Starting Applications....")
        self.apps("hello_world")
        print("Loaded Apps!")
        self.loadMenu()
    def boot(self):
        print("Ram Initializing!")
        self.initRAM(10)
        #bootSector == RAM[0] btw
        if RAM[0][0] == "print function param1=":
            print(RAM[0][1])
        else:
            print("Error")
            print(RAM[0])
            exit(-1)
    def initRAM(self, amount_of_data):
        global RAM
        RAM = [[0]] * amount_of_data
        print("Ram Initialized with", len(RAM), "amount's of data")
        self.loadKernel()
    def loadKernel(self):
        print("Kernel Loading....")
        bootBin = ["print function param1=",["Kernel Loaded into", len(RAM), "bits of ram!"]]
        RAM[0] = bootBin
        print("Kernel Loaded!")
    def apps(self, app):
        if app == "hello_world":
            worldData = "print function param1=","Hello World!"
            RAM[2] = worldData
        else:
            print("Invalid App Choice")
            exit(-1)
    def Menu(self):
        print("|----------------|")
        print("| 1. Hello World |")
        print("| 2. Shutdown    |")
        print("|________________|")
        print(" ")
        print(" ")
        app_select = input("Select a Number to do Something: ")
        if app_select == "1":
            self.loadApp("hello_world")
            self.Menu()
        elif app_select == "2":
            print("Unloading.....")
            RAM = 0
            print("Done Unloading RAM..")
            print("Exitting!")
            exit(1)
        else:
            print("Error invalid Selection!")
            self.Menu()
        
    def loadMenu(self):
        RAM[3] = "Variable Input function() Name:", "app_select"
        self.Menu()
    def loadApp(self, app):
        if app == "hello_world":
            if RAM[2][0] == "print function param1=":
                print(RAM[2][1])
MyOS = OS()
