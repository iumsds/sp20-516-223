from cloudmesh.common.Shell import Shell
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.dotdict import dotdict

dist = Shell.distribution()

VERBOSE(dist)
# Convert the dict to dotdict.
dist = dotdict(dist)

print(f"Platform is {dist.platform}")

if dist.platform == 'linux':
    if dist.ID == 'ubuntu':
        print('Nice you have ubuntu')
        if dist.VERSION_ID in ['"19.10"', '"18.04"']:
            print('and you have the right version as well. Good Job!')
        else:
            print('but you do not have the right version. Try harder!!!')
    else:
        print("You should use ubuntu")
elif dist.platform == 'windows':
    print("Good Luck!!!")
else:
    print("Unknown version")
