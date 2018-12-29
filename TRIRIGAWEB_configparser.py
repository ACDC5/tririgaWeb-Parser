def get_SSO():
    ssoVars = {}
    #This array can be modified with specific parameters to be checked for
    ssoParms = ["SSO_"]
    try:
        with open("tririgaWeb-Parser/TRIRIGAWEB.properties") as propFile:
            for line in propFile:
                #ignore comments and then check to see if any of the values in the parameterized array
                #are found in the line we're currently consuming. if so, store key/value pair in dict
                if "#" not in line:
                    if any(parm in line for parm in ssoParms):
                        param, value = line.partition("=")[::2]
                        ssoVars[param.strip()] = value

        for k, v in ssoVars.items():
            print (k,v)
    except IOError:
        print ("File not found")

def get_WFAgent():
    agentVars = {}
    #This array can be modified with specific parameters to be checked for
    agentParms = ["WFAgent","WF_AGENT"]
    try:
        with open("tririgaWeb-Parser/TRIRIGAWEB.properties") as propFile:
            for line in propFile:
                #ignore comments and then check to see if any of the values in the parameterized array
                #are found in the line we're currently consuming. if so, store key/value pair in dict
                if "#" not in line:
                    if any(parm in line for parm in agentParms):
                        param, value = line.partition("=")[::2]
                        agentVars[param.strip()] = value
        for k, v in agentVars.items():
            print (k,v)
    except IOError:
        print ("File not found")

print("Dumping SSO related key/value pairs:\n\n")
get_SSO()

print ("\nDumping workflow agent related key/value pairs:\n\n")
get_WFAgent()