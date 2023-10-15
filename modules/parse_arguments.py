import sys
import argparse

# Parse passed arguments
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_path", help="path to notes direcotry which should be scanned")
    parser.add_argument("--hist", help="output days since last edit histogram", action="store_true")
    parser.add_argument("--date", help="output creation by date plot", action="store_true")
    parser.add_argument("--month", help="output creation by month plot", action="store_true")
    parser.add_argument("--size", help="output note by size bar graph", action="store_true")
    parser.add_argument("--heatmap", help="output heatmap of note modification time", action="store_true")

    # Checks if enough arguments are passed
    if len(sys.argv)==2:
        parser.print_help()
        # parser.print_usage() # for just the usage line
        parser.exit()

    args = parser.parse_args()

    return args
