import os

os.system("pip3.11 freeze >  piplist.txt")
os.system("pipreqs ./ --encoding=utf8 --force")

with open('piplist.txt', 'r') as f:
    pip_list = f.read()

pip_dict = {}

for i in pip_list.split("\n"):
    try:
        module_name = i.split("==")[0]
        module_version = i.split("==")[1]
        pip_dict[module_name] = module_version
    except:
        pass
with open("requirements.txt", 'r') as f:
    pip_read = f.read()

pip_requirements = ""

for i in pip_read.split("\n"):
    module_name = i.split("==")[0]
    if module_name in pip_dict:
        pip_requirements += f"{module_name}=={pip_dict[module_name]}\n"

with open("requirements.txt", 'w') as f:
    f.write(pip_requirements)

os.remove("piplist.txt")