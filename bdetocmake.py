import os
import pystache

def createPackageCmakeLists(package, folder):
    pass

def getPackageComponents(package, folder):
    packagememfile = os.path.join(folder, "package", "{0}.mem".format(package))
    with open(packagememfile, 'r') as ff:
        components = ff.read().splitlines()
    return [comp for comp in components if comp[0] != '#']

def processGroup(group, folder, template):
    print("creating CMakeLists.txt for group {0}...".format(group))

    groupmemfile = os.path.join(folder, "group", "{0}.mem".format(group))
    with open(groupmemfile, 'r') as ff:
        packages = ff.read().splitlines()
        components = []
        for package in packages:
            if package[0] == '#':
                continue
            if group != package[:3]:
                print("found bad package name: {0}".format(package))
                continue
            comps = getPackageComponents(package, os.path.join(folder, package))
            components += ["{0}/{1}".format(package, comp) for comp in comps]

    groupdepfile = os.path.join(folder, "group", "{0}.dep".format(group))
    try:
        with open(groupdepfile, 'r') as ff:
            lines = ff.read().splitlines()
            deps = [dep for dep in lines if dep[0] != "#"]
    except:
        deps = []

    rendered = pystache.render(template, {
        'sourcefiles':  [{"name": comp} for comp in components],
        'packages':     [{"name": pkg} for pkg in packages],
        'dependencies': [{"name": dep} for dep in deps],
        'group':        group
    })

    with open(os.path.join(folder, "CMakeLists.txt"), 'w') as cmakefile:
        cmakefile.write(rendered)

def foo():
    with open("GroupCMakeTemplate.txt", 'r') as tempfile:
        template = tempfile.read()
    groups = os.listdir('groups')
    for gr in groups:
        processGroup(gr, os.path.join('groups', gr), template)

foo()
