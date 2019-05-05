#!/
def cleanPackageList(packageListDirty):
    packageList = [x.strip() for x in packageListDirty]
    packagesNoTags = (list(map(lambda p: p.split(" ")[0] , packageList)))
    return packagesNoTags


with open("./KevsChocoPackages.txt", 'r') as bulkPackageList:
    packageListDirty = bulkPackageList.readlines()

packages = cleanPackageList(packageListDirty)




with open ("chocoPackages.txt", "w+") as output:
    for package in packages:
        print ("{}\n".format(package))
        output.write("{}\n".format(package))
