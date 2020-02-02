import os

from cloudmesh.common.util import banner


# can be installed with pip install cloudmesh-common

class Provider:

    def __init__(self, name):
        self.name = name

    def start(self):
        banner(f"start {self.name}")
        os.system(f"multipass start {self.name}")
        print('\n')

    def delete(self, purge=True):
        banner(f"delete {self.name}")
        # terminate and purge
        # os.system(f"multipass delete {self.name}")
        # Once purged it cannot be recovered.
        # So we add a purge bool if we do not want o purge we set it to False
        if purge:
            os.system(f"multipass purge")
        print('\n')

    def list(self):
        # list instances
        banner("list")
        os.system("multipass ls")
        print('\n')

    def images(self):
        banner("images list")
        os.system("multipass find")
        print('\n')

    def shell(self):
        banner("shell")
        os.system(f"multipass shell {self.name}")
        print('\n')

    def run(self, command):
        # please add self.name so the command gets started on the named vm
        banner(f"run {self.name} {command}")
        # improve next line
        os.system(f"multipass exec -- {self.name} {command}")
        print('\n')


if __name__ == "__main__":
    p = Provider("e516")
    p.list()
    p.start()
    p.list()
    p.run("uname -r")
    p.images()
    p.delete(False)
    p.list()
