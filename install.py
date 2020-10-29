### Made by Sammy 🎃#6969 ###

try: 
    import requests
    import asyncio
    import os
    import sys
    import subprocess
    import zipfile
    from tqdm import tqdm as tqdm
except ImportError:  
    print("[>] The installer couldn't find a package (requests or asyncio or tqdm)! \n[>] The installer will try to install them, wait a minute!")
    os.system('py -m pip install requests')
    os.system('python -m pip install requests')
    os.system('pip install requests')
    
    os.system('py -m pip install tqdm')
    os.system('python -m pip install tqdm')
    os.system('pip install tqdm')
    
    os.system('py -m pip install asyncio')
    os.system('python -m pip install asyncio')
    os.system('pip install asyncio')


def IsSupported(platform):
    supported = {'win32' : 'Windows'}

    if platform not in supported:
            print("[>] Unsupported OS! Windows will work only.")
    else:
        pass


def DownloadAndInstall(what):
    os.system('cls')
    neoURL = "https://github.com/kem0o/neonitev2/archive/fdev.zip"
    nodeURL = "https://nodejs.org/dist/v12.19.0/node-v12.19.0-x64.msi"

    if what == "Neonite":
        chunk_size = 1024
        filesize = int(requests.head(neoURL).headers["Content-Length"])
        with requests.get(neoURL, stream=True) as r, open("Neonite.zip", "wb") as f, tqdm(
                unit="B",
                unit_scale=True,
                unit_divisor=1024, 
                total=filesize,
                file=sys.stdout,  
                desc="Neonite.zip" 
        ) as progress:
            for chunk in r.iter_content(chunk_size=chunk_size):
                datasize = f.write(chunk)
                progress.update(datasize)
        with zipfile.ZipFile("Neonite.zip", 'r') as NeoWork:
            NeoWork.extractall()
        os.rename("neonitev2-fdev", "Neonite")
    elif what == "node":
        chunk_size = 1024
        filesize = int(requests.head(nodeURL).headers["Content-Length"])
        with requests.get(nodeURL, stream=True) as r, open("node.msi", "wb") as f, tqdm(
                unit="B",
                unit_scale=True,
                unit_divisor=1024, 
                total=filesize,
                file=sys.stdout,  
                desc="Node Installer" 
        ) as progress:
            for chunk in r.iter_content(chunk_size=chunk_size):
                datasize = f.write(chunk)
                progress.update(datasize)
        print("[>] Instructions: Press Next, accept the terms and conditions and press all next then Install.")
        subprocess.call('node.msi', shell=True)


def ProceedWithUnzip(zipname):

    print('[>] Unzip placeholder!')

def IsInstalled(programName):
    doesExist = input("[>] (Y or N) The installer will now be looking for a Node installation. Do you have a custom installation PATH of Node? ")
    if doesExist == "N":
        path = f'{os.environ["ProgramFiles"]}\\node'
        if os.path.exists(path):
            print('\n[>] The installer found Node! We will proceed to install now Neonite.')
            pass
        else:
            wantsToContinue = input(f'[>] (Y or N) The installer didn''t find the PATH of Node. You want to continue? If yes, the installer will download Node and continue with the installation. ')
            if wantsToContinue == "Y":
                DownloadAndInstall("node")
            else:
                print("[>] Exiting...")
    elif doesExist == "Y":
        path = input('[>] Okay! Input the PATH please: ')
        if os.path.exists(path):
            print('\n[>] The installer found Node! Continuing...')
        else:
            print("[>] The PATH does not exist! Exiting....")
            exit()

        
## Start the script ##
#   |_ Checking for the OS, if not Windows quit. ##
#   |_ Check for Node, if not the script is going to install it automatically.
#
#
os.system('cls')
print("\nWelcome to the Unofficial Neonite Installer!\n")
print(f"Platform: {sys.platform}")
print(f"Current Directory: {os.path.abspath(os.getcwd())} \n")
IsSupported(sys.platform)

IsInstalled("Node")
print("[>] The installer successfully installed Node!")
os.remove('node.msi')

DownloadAndInstall('Neonite')
print("[>] The installer successfully downloaded Neonite!")
os.remove('Neonite.zip')
exit()

