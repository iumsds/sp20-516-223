import platform
import re
import subprocess

from flask import jsonify, json
from flask import Flask, current_app


def get_processor_name():
    print(f"Inside get processor : {platform.system()}")
    if platform.system() == "Windows":
        p = platform.processor()
    elif platform.system() == "Darwin":
        command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
        p = subprocess.check_output(command, shell=True).strip().decode()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip().decode()
        for line in all_info.split("\n"):
            if "model name" in line:
                p = re.sub(".*model name.*:", "", line, 1)
    else:
        p = "Unable to find the processor name."

    pinfo = {"model" : p}

    return jsonify(pinfo)

if __name__ == "__main__":
    app = Flask(__name__)

    with app.app_context():
        # within this block, current_app points to app.
        print(current_app.name)
        pinfo = get_processor_name()
        print(pinfo.get_data(as_text=True))

