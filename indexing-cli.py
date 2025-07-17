import argparse
import os
import glob as _glob
from datetime import datetime

def InitParser():
    # ------- cli specific parsing ---------
    parser = argparse.ArgumentParser(prog="File Ordering CLI")
    # directory group
    dirs = parser.add_argument_group("Directory")
    dirs.add_argument('-s','--src-dir', type=str, default=os.getcwd(), help="Source directory to read files from.")
    # file type group
    ftypes = parser.add_argument_group("File Types")
    ftypes.add_argument('-sft','--source-file-type', type=str, help="Source file type to select from list of files in directory.")
    # order group
    order = parser.add_argument_group("Ordering")
    order.add_argument('-st', '--start', type=int, help="Order the target from starting given number.")
    order.add_argument('-r', '--reverse-ordering', type=bool, default=False, help="Reverse ordering, takes 1 for True, 0 for False")
    order.add_argument('-re', '--reorder', type=int, nargs="+", metavar="FROM TO")
    order.add_argument('-f', '--format', type=str)
    # ----------------------------------------

    args = parser.parse_args()
    return args

# simple chunk function
def chunks(xs, n):
    n = max(1, n)
    return (xs[i:i+n] for i in range(0, len(xs), n))

def order_by_int(x, fr):
    name, ext = os.path.splitext(os.path.basename(x))
    try:
        int(name)
    except:
        print(name)
        return datetime.strptime(name,fr)
    else:
        return int(name)

if __name__ == "__main__":
    args = InitParser()
    # check the correctness of source path 
    if os.path.exists(args.src_dir):
        src_dir = args.src_dir
    else:
        raise Exception("Source Path dont exist")


    # handle source file type
    if args.source_file_type:
        name, ext = os.path.splitext(args.source_file_type)
        if not ext:
            source_file_type = name
    else:
        source_file_type = ".png"

    print(source_file_type)
    # order reverse from start point
    reverse = args.reverse_ordering

    ordered_source_list = _glob.glob(os.path.join(src_dir, "*"+source_file_type))
    ordered_source_list.sort(key=lambda x: order_by_int(x, args.format))

    source_list = []

    # Add "_" to name
    # ["./places/almaty/raw/1.png", "./places/almaty/raw/2.png", ...]
    for index, i in enumerate(ordered_source_list):
        name, ext = os.path.splitext(i)
        new_i = os.path.join(name+"_"+ext) 
        os.rename(i, new_i)

        # with this ordered_source_list and source_list are same, except _ character in the end of file name.
        source_list.append(new_i)

    # reorder the given numbers
    if args.reorder:
        if len(args.reorder)%2 != 0:
            raise Exception("Reorder arguments must be odd") 
        else:
            for chunk in chunks(args.reorder, 2):

                from_order = chunk[0] - 1
                to_order = chunk[1] - 1 

                popped_item = ordered_source_list.pop(from_order)
                ordered_source_list.insert(to_order, popped_item)

                second_popped_item = source_list.pop(from_order)
                source_list.insert(to_order, second_popped_item)

    for index, x in enumerate(ordered_source_list):
        if reverse:
            number = args.start - index
        else:
            number = args.start + index

        name, ext = os.path.splitext(x)
        new_x = os.path.join(os.path.dirname(x),str(number)+ ext)
        os.rename(source_list[index], new_x) 
        print(f'{source_list[index]} renamed to {new_x}')
