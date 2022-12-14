from kazmoduleloader import Loader
import logging

loader = Loader()
logger = logging.getLogger("KazIDE")
logger.setLevel(logging.DEBUG)
loader.setLogger(logger)


def main():
    loader.loadDir()
    loader.setupModules()


if __name__ == "__main__":
    main()
