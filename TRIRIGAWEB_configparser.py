#Let's declare us some variables!
ssoVars = {}
agentVars = {}
eachAndEveryVar = {}
ssoFUBAR = False

"""
This function retrieves certain SSO settings from the properties file
"""
def get_SSO():
    #This array can be modified with specific parameters to be checked for
    ssoParms = ["SSO_"]
    try:
        with open("tririgaWeb-Parser/TRIRIGAWEB.properties") as propFile:
            for line in propFile:
                #ignore comments and then check to see if any of the values in the parameterized array
                #are found in the line we're currently consuming. if so, store key/value pair in dict
                if "#" not in line:
                    if any(parm in line for parm in ssoParms):
                        key, value = line.partition("=")[::2]
                        ssoVars[key.strip()] = value.strip()
    except IOError:
        print ("File not found")
    for k, v in ssoVars.items():
            print (k,v)
"""
This function retrieves certain Workflow agent settings from the properties file
"""
def get_WFAgent():
    #This array can be modified with specific parameters to be checked for
    agentParms = ["WFAgent","WF_AGENT"]
    try:
        with open("tririgaWeb-Parser/TRIRIGAWEB.properties") as propFile:
            for line in propFile:
                #ignore comments and then check to see if any of the values in the parameterized array
                #are found in the line we're currently consuming. if so, store key/value pair in dict
                if "#" not in line:
                    if any(parm in line for parm in agentParms):
                        key, value = line.partition("=")[::2]
                        agentVars[key.strip()] = value.strip()
    except IOError:
        print ("File not found")
    for k, v in agentVars.items():
            print (k,v)

"""
This function validates that SSO parameters aren't setup to conflict with each other
i.e., remote_user and user_principal both being set to 'Y'
"""
def check_SSO():
    global ssoFUBAR
    if ssoVars.get("SSO_REMOTE_USER") is "Y" and ssoVars.get("SSO_USER_PRINCIPAL") is "Y":
        #print ("HEY. DONT DO THAT. REMOTE_USER AND USER_PRINCIPAL CANT BOTH BE YES\n\n")
        ssoFUBAR = True
    else:
        print ("All good.\n")
        ssoFUBAR = False
    


"""
This function retrieves all 'useful' parameters at once. Currently unused
"""

def get_all():
    allParms = ["WFAgent","WF_AGENT","SSO_"]
    try:
        with open("tririgaWeb-Parser/TRIRIGAWEB.properties") as propFile:
            for line in propFile:
                #ignore comments and then check to see if any of the values in the parameterized array
                #are found in the line we're currently consuming. if so, store key/value pair in dict
                if "#" not in line:
                    if any(parm in line for parm in allParms):
                        key, value = line.partition("=")[::2]
                        eachAndEveryVar[key.strip()] = value.strip()
    except IOError:
        print ("File not found")
    for k, v in eachAndEveryVar.items():
            print (k,v)


def lul_test():
    print("Wow...a  test harness. Fucking took you long enough.")

    print("Dumping SSO related key/value pairs:\n\n")
    get_SSO()

    print ("\nDumping workflow agent related key/value pairs:\n\n")
    get_WFAgent()

    print ("\nChecking for conflicting SSO settings:\n\n")
    check_SSO()

    print ("\nMake sure that get_all works:\n\n")
    get_all()

    if ssoFUBAR:
        print ("SSO parameter conflicts detected. Review.")

lul_test()