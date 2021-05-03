import subprocess


class Serial:
    @staticmethod
    def out(medicine_list, dev_list):
        out_str = "sudo -S "
        result = subprocess.run("which serdvr.out", shell=True, capture_output=True, text=True)

        out_str += result.stdout + "/serdvr.out "
        print(out_str)

        for el in dev_list:
            out_str += (el + " ")

        for el in medicine_list:
            out_str += (el + " ")

        # out_list = ["sudo", "-S", "/home/alexander/Documents/VMKS/DesktopApp/serdvr.out"]
        # out_list += dev_list
        # out_list += medicine_list
        print(out_str)

        subprocess.run(out_str, shell=True)
        return 0
