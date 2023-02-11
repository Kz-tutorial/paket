import os,time,sys



os.system("clear")
print("[\033[91m•\033[97m] \033[92mIklan Dulu Baru Masuk ")
time.sleep(2)
os.system("xdg-open https://tokopedia.link/EJDZVehvkxb")
time.sleep(2)
os.system("clear")
def install_packages():
    packages = ['python', 'nano', 'wget', 'git', 'curl', 'unzip', 'tar',
                'vim', 'openssh', 'sshpass', 'php', 'ruby', 'nodejs',
                'clang', 'golang', 'tmux', 'screen', 'htop',
                'ncurses-utils', 'figlet']
    packages2 = ['requests', 'mechanize', 'pytube']

    for package in packages:
        print()
        print(f"\033[97m[\033[91m•\033[97m] \033[92m{package} \033[92mterinstall\033[93m ✓\033[96m")
        print()
        os.system(f"pkg install {package}")

    for packages in packages2:
        print(f"\033[96mPackage {packages} terinstall\033[0m")
        print(f"\033[97m[\033[91m•\033[97m] \033[92m{package} \033[92mterinstall\033[93m ✓\033[96m")
if __name__ == '__main__':
    install_packages()
