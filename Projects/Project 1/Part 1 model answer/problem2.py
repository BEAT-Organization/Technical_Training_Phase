import re #package used to find patterns in strings

sequence= "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT" #sequence
artifact = "GAATTC" #the part the enzyme will cut the sequence at


x = re.search(artifact, sequence).span #index of the GAATTC in the sequence

artifacts = [sequence[0 : (x(0)[0] + 1)], sequence[(x(0)[0] + 1):]] #splitting at x(0)[0] + 1 which is the index of the neuclutide after G

print(artifacts)
print(len(artifacts[0]), len(artifacts[1]))