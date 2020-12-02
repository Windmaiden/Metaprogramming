import logging
from inspect import (
    getmembers,
    isfunction,
)
from os import (
    listdir,
    walk,
)
from os.path import (
    isdir,
    join,
)
from time import time

from go import verification
from go.objects.go_file import GoFile


class Analyser:
    """ Go analyser
    Attributes
        VERIFY: Mode for only check files
        FIX: Mode for fix files
        verifications: List of verification functions from
                       verification module
        verify_logger: Return logger for verify mode
        fix_logger: Return logger for fix mode

    Methods
        scan_project(path, mode)
        scan_dir(path, mode)
        scan_file(path, mode)
    """
    VERIFY = 0
    FIX = 1

    verifications = [o[1] for o in getmembers(verification) if isfunction(o[1])]

    @property
    def verify_logger(self) -> logging.Logger:
        """ Logger for check code """
        logger = getattr(self, "_verify_logger", None)
        if logger is None:
            logger = logging.getLogger("verification")
            logger.setLevel(logging.INFO)
            fh = logging.FileHandler(f'verification_{int(time())}.log')
            logger.addHandler(fh)
            self._verify_logger = logger
        return logger

    @property
    def fix_logger(self) -> logging.Logger:
        """ Logger for fixes """
        logger = getattr(self, "_fix_logger", None)
        if logger is None:
            logger = logging.getLogger("fix")
            logger.setLevel(logging.INFO)
            fh = logging.FileHandler(f'fix_{int(time())}.log')
            logger.addHandler(fh)
            self._fix_logger = logger
        return logger

    @classmethod
    def scan_project(cls, path: str, mode: int):
        """ Scan project """
        if not isdir(path):
            raise ValueError("Path is not dir")

        instance = cls()
        for root, dirs, files in walk(path):
            for file_name in files:
                path_to_file = join(root, file_name)
                if GoFile.is_go_file(path_to_file):
                    instance._scan_go_file(GoFile(path_to_file), mode)

    @classmethod
    def scan_dir(cls, path: str, mode: int):
        """ Scan directory """
        if not isdir(path):
            raise ValueError("Path is not dir")

        instance = cls()
        for file_name in listdir(path):
            path_to_file = join(path, file_name)
            if GoFile.is_go_file(path_to_file):
                instance._scan_go_file(GoFile(path_to_file), mode)

    @classmethod
    def scan_file(cls, path: str, mode: int):
        """ Scan one file """
        instance = cls()
        if GoFile.is_go_file(path):
            instance._scan_go_file(GoFile(path), mode)
        else:
            raise ValueError("Path is not go file")

    def _scan_go_file(self, go_file: GoFile, mode: int):
        """ Verify go file """
        for verification_func in self.verifications:
            for verification_error in verification_func(go_file):
                if mode == self.VERIFY:
                    self.verify_logger.info(verification_error.message)
                elif mode == self.FIX:
                    if verification_error.fix():
                        self.fix_logger.info(verification_error.message)

        if mode == self.FIX:
            with open(f"{go_file.path}", "w", encoding='utf-8') as file:
                file.write(str(go_file))
