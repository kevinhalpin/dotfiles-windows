print("----------------------------------")
print("Beginning Python Script To Sanatize")

def cleanPackageList(packageListDirty):
    packageList = [x.strip() for x in packageListDirty]
    packagesNoTags = (list(map(lambda p: p.split(" ")[0] , packageList)))
    return packagesNoTags


with open("./ChocoPackagesToInstall.txt", 'r') as bulkPackageList:
    packageListDirty = bulkPackageList.readlines()

packages = cleanPackageList(packageListDirty)

with open ("./SanitizedChocoPackagesToInstall.txt", "w+") as output:
    for package in packages:
        print ("{}\n".format(package))
        output.write("{}\n".format(package))

print("Choco Programs sanitized")
print("----------------------------------")