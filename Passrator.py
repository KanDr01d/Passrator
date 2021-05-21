########################################################################
########################################################################
import secrets, string, datetime, sys, numbers, importlib,os        ####
from time import sleep                                              ####
from os import name                                                 ####
try:                                                                ####
    import termcolor                                                ####
    from termcolor import cprint                                    ####
except ImportError or ModuleNotFoundError:                          ####
    os.system ('pip3 install termcolor')                            ####
    import termcolor                                                ####
    from termcolor import cprint                                    ####
finally:                                                            ####
    pass                                                            ####
########################################################################
########################################################################

#Checking Default Setting
def ChSet():
    global Loop, Lp, SaPa   
    try:
        from Autosave import ASLoop,ASLp, ASSaPa
        Loop = ASLoop
        Lp = ASLp
        SaPa = ASSaPa
    except:
        Loop = 1
        Lp = "Disable"
        SaPa = "Disable"
    finally:
        pass

#Error 1: Not vaid command
def ErrorNoti():
        cprint ("Not valid command, try again", 'red')
        sleep (1)
        clear()

#Error 2: Not vaid
def ErrorNoti2():
        cprint ("Not valid, try again", 'red')
        sleep (1)
        clear()

#Define clear function 
def clear(): 
  
    #Windows 
    if name == 'nt': 
        _ = os.system('cls') 
  
    #Mac and Linux
    else: 
        _ = os.system('clear')
        
#Start
def MenuStart():
    clear()
    global TypePass, Selecte
    TypePass = ""
    Selecte = ""
    cprint ("██████╗░░█████╗░░██████╗░██████╗██████╗░░█████╗░████████╗░█████╗░██████╗░", 'green')
    cprint ("██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗", 'green')
    cprint ("██████╔╝███████║╚█████╗░╚█████╗░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝", 'green')
    cprint ("██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗", 'green')
    cprint ("██║░░░░░██║░░██║██████╔╝██████╔╝██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║", 'green')
    cprint ("╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝", 'green')
    cprint ("[N] PIN mode (Only number)", 'blue')
    cprint ("[P] Password mode (Charaters, numbers and special characters)", 'blue')
    cprint ("[S] Setting", 'cyan')
    cprint ("[E] Exit", 'red')
    Selecte = input (">> ") 

    if Selecte == "N":
        TypePass = "PIN"
        PINMode()
        exit (0)
    elif Selecte == "P":
        TypePass = "Password"
        PasswordMode()
        exit(0)
    elif Selecte == "S":
        Setting()
    elif Selecte == "E":
        try:
            clear()
            exit (0)
        except IOError:
            pass
        except ValueError:
            pass
        finally:
            clear()
            SystemExit()
            pass
    else:
        ErrorNoti()
        MenuStart()

#Length for PIN mode
def LNMode():   
    global Length
    clear()
    cprint ("Minimum: 4", 'magenta')
    Length = input("Length: ")
    if Length.isdigit () == True:
        Length = int(Length)
        pass
    else:
        ErrorNoti()
        LNMode()
    return Length

#PIN Mode
def PINMode():
    global Password, Loop, SaPa, Lp
    ChSet()
    LNMode()
    while Length < 4:
        cprint ("Not valid. Try again", 'blue')
        sleep(0.1)
        LNMode()
    else:
        Loop = int (Loop)
        for Password in range (Loop):
            PIN = string.digits
            Password =  ''.join(secrets.choice(PIN) for Password in range(Length))
            print (Password, "\n")
            if SaPa == "Active":
                SavePassword()
            else:
                pass

#Special Charaters option
def SpecialCharaters():
    global SpCh
    SpCh =  input("Active special characters option? (Y/N): ")
    if SpCh.isalpha () == True:
        pass
    else:
        ErrorNoti2()
        SpecialCharaters()
    return SpCh

#Length for Password mode
def LPMode():
    global Length
    clear()
    cprint ("Minimum: 8. Numbers is default in password generation. Special characters is an optional option.", 'magenta')
    Length = input("Length: ")
    if Length.isdigit () == True:
        Length = int(Length)
        pass
    else:
        ErrorNoti2()
        LPMode()
    return Length

#Password mode
def PasswordMode():
    global Password, Loop, SaPa, Lp
    ChSet()
    LPMode()
    while Length < 8:
        ErrorNoti2()
        LPMode()
    else:
        SpecialCharaters()
        while SpCh != "N" and SpCh != "Y":
            ErrorNoti()
            SpecialCharaters()
        if SpCh == "Y":
            Loop = int(Loop)
            for Password in range(Loop):
                RandomString = string.ascii_letters + string.punctuation  + string.digits
                Password =  ''.join(secrets.choice(RandomString) for Password in range(Length))
                print (Password, "\n")
                if SaPa == "Active":
                    SavePassword()
                else:
                    pass 
            
        elif SpCh == "N":
            Loop = int(Loop)
            for Password in range (Loop):
                RandomString = string.ascii_letters + string.digits
                Password =  ''.join(secrets.choice(RandomString) for password in range(Length))
                print (Password, "\n")
                if SaPa == "Active":
                    SavePassword()
                else:
                    pass
                
#Setting optional
def Setting():

    #AutoSave Setting
    def ATSSetting():
        AS = open ("Autosave.py","w")
        AS.write ("ASLoop = ")
        AS.write (str(Loop))
        AS.write ("\nASLp = \"")
        AS.write (Lp)
        AS.write ("\"\nASSaPa = \"")
        AS.write (SaPa)
        AS.write ("\"")

    #Reload module after every update status
    def UpdModule():
        global Loop, Lp, SaPa
        import Autosave
        importlib.reload(Autosave)
        from Autosave import ASLoop,ASLp,ASSaPa
        Loop = ASLoop
        Lp = ASLp
        SaPa = ASSaPa
        return Loop, Lp, SaPa

    #Clear screen and return to Setting
    def CAS():
        global Loop, Lp, SaPa
        clear()
        ATSSetting()
        UpdModule()
        MenuSetting()

    # M E N U     S E T T I N G 
    def MenuSetting():
        global Loop, Lp, SaPa, Selecte
        Selecte = ""
        clear()
        ChSet()
        cprint ("[L] Loop: ", 'yellow', end = '')
        print (Lp)
        if Lp == "Active":
            cprint ("[LT] Loops time: ", 'yellow', end = '')
            print (Loop)
        cprint ("[SP] Save Password mode: ", 'yellow', end = '')
        print (SaPa)
        cprint ("[M] Menu", 'yellow')        
        Selecte = input ("  >>  ")        

        if Selecte == "L":
            clear()
            if Lp == "Disable":
                Setting = input ("Active Loop? [Y/N]     ")
                if Setting  == "Y":
                    Lp = "Active"
                    print ("Loop time(s):", Loop)
                    cprint ("If you input 1, that will automatically changed back to default setting", 'white', 'on_red')
                    Loop = input ("New loop times? : ")
                    while Loop.isdigit() == False:
                        cprint ("Integer, please", 'red')
                        Loop = 1
                        Lp = "Disable"
                        sleep (1)
                        CAS()
                    else:
                        while Loop == 1:
                            Lp = "Disable"
                            CAS()
                        else:
                            CAS()
                else:
                    CAS()

            elif Lp == "Active":
                Setting = input ("Disable Loop? [Y/N]     ")
                if Setting == "Y":
                    Loop = 1
                    Lp = "Disable"
                    CAS()
                else:
                    print ("Loop time(s):", Loop)
                    cprint ("If you input 1, that will automatically changed back to default setting", 'white', 'on_red')
                    NewLoop = input ("New loop times? : ")
                    while NewLoop.isdigit() == False:
                        cprint ("Integer, please", 'red')
                        Lp = "Active"
                        sleep (1)
                        CAS()
                    else:
                        if NewLoop == 1:
                            Loop = 1
                            Lp = "Disable"
                            CAS()
                        else:
                            Loop = NewLoop
                            CAS()

        if Selecte == "LT":
            clear()
            if Lp == "Disable":
                CAS()
            else:
                cprint ("If you input 1, that will automatically changed back to default setting", 'white', 'on_red')
                Loop = input ("New loop times? : ")
                while Loop.isdigit() == False:
                    cprint ("Integers, please", 'red')
                    Lp = "Disable"
                    Loop = 1
                    sleep (1)
                    CAS()
                else:
                    Loop = int (Loop)
                    if Loop > 1:
                        CAS()
                    else:
                        Loop = 1
                        Lp = "Disable"
                        CAS()            

        if Selecte == "SP":
            clear ()
            if SaPa == "Disable":
                Setting = input("Active Save Password? [Y/N]     ")
                if Setting == "Y":
                    SaPa = "Active"
                elif Setting == "N":
                    pass
                else:
                    cprint("Error: Command not found", 'white', 'on_red')
                    sleep (1)
                    CAS ()
            elif SaPa == "Active":
                Setting = input("Disable Save Password? [Y/N]     ")
                if Setting == "Y":
                    SaPa = "Disable"
                elif Setting == "N":
                    pass
                else:
                    cprint("Error: Command not found", 'white', 'on_red')
                    sleep (1)
                    CAS ()
            CAS()

        if Selecte == "M":
            clear()
            MenuStart()
            
        else:
            cprint ("Cant detect command, try again", 'red')
            sleep (2)
            CAS()
    MenuSetting()

#Save Password
def SavePassword():
    global TypePass
    LogTime = datetime.datetime.now().strftime("%c")
    PF = open("Password.txt","a")
    PF.write (LogTime)
    PF.write ("|\t")
    PF.write ("Type: ")
    PF.write (TypePass)
    if TypePass=="PIN":
        PF.write ("\t\t|\t")
    elif TypePass=="Password":
        PF.write ("  |\t")
    PF.write (Password)
    PF.write ("\n")
    PF.close

#######################################################################################################################################################################################################################################################################
MenuStart()
