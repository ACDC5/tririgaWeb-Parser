#Let's declare us some variables!
ssoVars = {}
wfAgentVars = {}
ssoParms = []
agentParms = []
eachAndEveryVar = {}
ssoFUBAR = False

"""
This function retrieves certain SSO settings from the properties file
"""
def get_SSO():
    global ssoParms
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
    global agentParms
    #This array can be modified with specific parameters to be checked for
    agentParms = ["WFAgent","WF_AGENT", "WF_INSTANCE_SAVE"]
    try:
        with open("tririgaWeb-Parser/TRIRIGAWEB.properties") as propFile:
            for line in propFile:
                #ignore comments and then check to see if any of the values in the parameterized array
                #are found in the line we're currently consuming. if so, store key/value pair in dict
                if "#" not in line:
                    if any(parm in line for parm in agentParms):
                        key, value = line.partition("=")[::2]
                        wfAgentVars[key.strip()] = value.strip()
    except IOError:
        print ("File not found")
    for k, v in wfAgentVars.items():
            print (k,v)

"""
This function validates that SSO parameters aren't setup to conflict with each other
i.e., remote_user and user_principal both being set to 'Y'
"""
def check_SSO():
    global ssoFUBAR
    if ssoVars.get("SSO_REMOTE_USER") is "Y" and ssoVars.get("SSO_USER_PRINCIPAL") is "Y":
        ssoFUBAR = True
    else:
        print ("All good.\n")
        ssoFUBAR = False
    if ssoFUBAR:
        print ("SSO parameter conflicts detected. Review.\n")

def check_WF():
    if wfAgentVars.get("WF_INSTANCE_SAVE") != "ERRORS_ONLY":
        print("WARNING: Workflow instance saving is set to " + wfAgentVars.get("WF_INSTANCE_SAVE") + ". It should be set to ERRORS_ONLY")
    else:
        print("All good.\n")

"""
This function retrieves all 'useful' parameters at once.
"""

def get_all():
    allParms = ssoParms + agentParms
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

    print ("\nChecking for conflicting SSO settings:\n")
    check_SSO()

    print ("\nValidating WF/WF_Agent settings:\n")
    check_WF()

    print ("\nMake sure that get_all works:\n")
    get_all()



lul_test()