import subprocess

if __name__ == '__main__':
    result = subprocess.run(["serialdrv/serdrv", "Vasko"])

    stat = result.check_returncode()
    if stat != None:
        print ("ERROR #{}".format(stat))