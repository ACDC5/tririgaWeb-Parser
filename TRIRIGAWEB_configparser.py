def get_SSO():
    tririgaVars = {}
    with open("TRIRIGAWEB.properties") as propFile:
        for line in propFile:
            if "#" not in line:
                if "SSO_" in line:
                    param, value = line.partition("=")[::2]
                    tririgaVars[param.strip()] = value

    for k, v in tririgaVars.items():
        print (k,v)

get_SSO()
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