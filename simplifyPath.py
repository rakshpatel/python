
def simplifyPath(path):
    path = path.split("/")
    outputString=''
    parentDir = 0
    #path = [val for val in path if val]
    print(path)
    while path:
        val = path.pop()
        if val == "..":
            parentDir += 1
        elif not val or val == ".":
            continue
        else:
            if not parentDir:
                outputString = "/" + val + outputString
            else:
                parentDir -= 1
    if not outputString:
        return "/"
    
    return outputString

'''
def simplifyPath(path):
    output = []
    for val in path.split("/"):
        if not val:
            continue
        elif val == "..":
            if output:
                output.pop()
        else:
            if val != ".":
                output.append(val)
    return "/"+"/".join(output)
'''

if __name__ == "__main__":
    path = "/home/"
    print(simplifyPath(path))

    path = "/../"
    print(simplifyPath(path))

    path = "/home//foo/"
    print(simplifyPath(path))

    path = "/a/./b/../../c/"
    print(simplifyPath(path))

    path = "/a/../../b/../c//.//"
    print(simplifyPath(path))
    
    path = "/a//b////c/d//././/.."
    print(simplifyPath(path))