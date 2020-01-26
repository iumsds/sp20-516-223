import os
class Provider:
  def list(self):
    print("list")
    os.system("ls")

  def shell(self):
    print("shell")
    os.system("sh")

  def run(self, command):
    print(f"run {command}")
    os.system(f"exec {command}")

## Main
if __name__ == "__main__":
  p = Provider()
  p.run("pwd")
  p.list()
    
