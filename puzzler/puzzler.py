import os
import glob

class puzzler:

    addonFolder = "addons"
    className =  "addon"
    addons = []
    
    def __init__(self):
        self.loadAddons()

    def loadAddons(self):
        # print glob('addons')
        dirPath = os.path.dirname(os.path.realpath(__file__))
        addonPath = os.path.join(dirPath, self.addonFolder)
        ignore = ["__init__"]
        for file in glob.glob("{}{}*.py".format(addonPath,os.sep)):
            importName = os.path.splitext(os.path.basename(file))[0]
            # ignore
            if importName in ignore:
                continue
            # import
            test = "{}.{}".format(self.addonFolder,importName,importName)
            addon = __import__(test, fromlist=[importName])
            mod = getattr(addon, importName)
            # append to addon list
            self.addons.append({
                "name": importName,
                "module": mod,
                "methods": dir(mod),
            })

    def getAddon(self, name):
        for addon in self.addons:
            if addon["name"] == name:
                return addon
        return False
            
    def getAddons(self, module=True):
        if module:
            return self.addons
        else:
            formatted = []
            for addon in self.addons:
                formatted.append({
                    "name": addon["name"],
                    "methods": addon["methods"],
                })
            return formatted

    def printAddons(self):
        for addon in self.addons:
            print addon

main = puzzler()