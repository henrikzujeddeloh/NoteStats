import argparse

# Parse passed arguments
def parse_arguments():
    parser = argparse.ArgumentParser()

    # Define arguments
    parser.add_argument("folder_path", help="path to notes directory which should be scanned")
    parser.add_argument("--date", help="output creation by date plot", action="store_true")
    parser.add_argument("--month", help="output creation by month plot", action="store_true")
    parser.add_argument("--size", help="output note by size bar graph", action="store_true")
    parser.add_argument("--hist", help="output days since last edit histogram", action="store_true")
    parser.add_argument("--heatmap", help="output heatmap of note modification time", action="store_true")


    args = parser.parse_args()

    return args


# Ask user to select a new visualization or quit
def select_next_visualization():

    print("Would you like to output another visualization?\nPlease select what to output (1-5) or 'q' to quit")
    selection = input("1 - date\n2 - month\n3 - size\n4 - hist\n5 - heatmap\n")
    return selection


# Update argument to new selection
def update_args(args, selection):
    args.date = False
    args.month = False
    args.size = False
    args.hist = False
    args.heatmap = False

    if selection == '1':
        args.date = True

    if selection == '2':
        args.month = True

    if selection == '3':
        args.size = True
   
    if selection == '4':
        args.hist = True

    if selection == '5':
        args.heatmap = True

    return args

