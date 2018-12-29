def get_SSO():
    ssoVars = {}
    #This array can be modified with specific parameters to be checked for
    ssoParms = ["SSO_"]
    try:
        with open("tririgaWeb-Parser/TRIRIGAWEB.properties") as propFile:
            for line in propFile:
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
                if "#" not in line:
                    if any(parm in line for parm in agentParms):
                        param, value = line.partition("=")[::2]
                        agentVars[param.strip()] = value
                    """if "WFAgent" in line:
                        param, value = line.partition("=")[::2]
                        agentVars[param.strip()] = value
                    if "WF_AGENT" in line:
                        param, value = line.partition("=")[::2]
                        agentVars[param.strip()] = value"""
        for k, v in agentVars.items():
            print (k,v)
    except IOError:
        print ("File not found")

print("Dumping SSO related key/value pairs:\n\n")
get_SSO()

print ("\nDumping workflow agent related key/value pairs:\n\n")
get_WFAgent()
"""
for k, v in tririgaVars.items():
    if "Y" in v:
        print (k)
        print (v)
"""

"""
if "Y" in tririgaVars.get("SSO_REMOTE_USER"):
    print ("yes")
"""