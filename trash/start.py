import subprocess
import sys

# Game required packages
packagesToInstall = ["colorama"]


# Will install required packages before the game started.
def installPackages(packages: list):
    """Function that will accept list of packages, try to import and if they are not installed will install them."""
    for package in packages:
        try:
            import package
        except ImportError as e:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Check and install required packages
installPackages(packagesToInstall)

if __name__ == '__main__':
    import main
    main.doStart()
