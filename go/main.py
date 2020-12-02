from argparse import ArgumentParser

from go.analyser import Analyser


def main():
    """ Program entrypoint

    usage: main.py [-h] (--verify | --fix) (-f | -d | -p) path

    positional arguments:
      path           Path to file/folder

    optional arguments:
      -h, --help     show this help message and exit
      --verify       Verify files.
      --fix          Auto fix files.
      -f, --file     Analyze file only.
      -d, --dir      Analyze folder.
      -p, --project  Analyze project.
    """
    arg_parser = ArgumentParser()
    group_mode = arg_parser.add_mutually_exclusive_group(required=True)
    group_mode.add_argument("--verify", help="Verify files.",
                            action="store_true")
    group_mode.add_argument("--fix", help="Auto fix files.",
                            action="store_true")
    group_file_mode = arg_parser.add_mutually_exclusive_group(required=True)
    group_file_mode.add_argument("-f", "--file", action="store_true",
                                 help="Analyze file only.")
    group_file_mode.add_argument("-d", "--dir", action="store_true",
                                 help="Analyze folder.")
    group_file_mode.add_argument("-p", "--project", action="store_true",
                                 help="Analyze project.")
    arg_parser.add_argument("path", help="Path to file/folder")
    args = arg_parser.parse_args()

    if args.verify:
        mode = Analyser.VERIFY
    elif args.fix:
        mode = Analyser.FIX
    else:
        raise ValueError("Args not set mode, --fix/--verify")

    if args.file:
        Analyser.scan_file(args.path, mode)
    elif args.dir:
        Analyser.scan_dir(args.path, mode)
    elif args.project:
        Analyser.scan_project(args.path, mode)
