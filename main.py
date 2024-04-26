import sys
from built_in_func import builtin_switch
from data_structures import ds_switch

def main(option_file, option_arg):
    # Call switch case functions based on the input argument
    if option_file == 'builtin':
        builtin_switch(option_arg)
    if option_file == 'ds':
        ds_switch(option_arg)
    else:
        print(f"Invalid argument: {option_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <argument> <argument>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
