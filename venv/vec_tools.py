import numpy as np
import argparse
import sys
import os



def set_datatype(datatype_str):
    if datatype_str == "complex128":
        return np.complex128
    if datatype_str == "complex64":
        return np.complex64
    if datatype_str == "float32":
        return np.float32
    if datatype_str == "float64":
        return np.float64
    else :
        sys.exit("datatype \""+ datatype_str + "\" is not recognized, aborting!")

def clean_file(filepath):
    with open(filepath) as f:
        newtxtarr = f.read().replace('+-', '-')

    with open(filepath, "w") as f:
        f.write(newtxtarr)


def manipulate_txt_arrays(filename1, filename2, op, datatype):
    print("datatype = ", datatype, type(datatype))
    arr1 = np.loadtxt(filename1, dtype=datatype)
    arr2 = np.loadtxt(filename2, dtype=datatype)
    if arr1.shape != arr2.shape :
        print ("arr1.shape = ", arr1.shape)
        print ("arr2.shape = ", arr2.shape)
        sys.exit("input arrays have incompatible shapes, aborting!")

    np.savetxt(filename1 + "_out", arr1)
    np.savetxt(filename2 + "_out", arr2)
    print("===== arr1 =====\n", arr1)
    print("===== arr2 =====\n", arr2)
    if op == "+":
        return arr1 + arr2
    elif op == "-":
        return arr1 - arr2
    elif op == "dot" :
        return np.dot(arr1,arr2)
    elif op == "vdot" :
        return np.vdot(arr1,arr2)
    else :
        sys.exit("operation \"" +op+ "\" is not defined, aborting!")


usage = 'manipulate_arrays --f1=filename1  --f2=filename2 --op=+,-,dot  --datatype=datatype (will do f1 op f2)'

parser = argparse.ArgumentParser( usage, formatter_class=argparse.ArgumentDefaultsHelpFormatter )

parser.add_argument('--f1',
                   action='store',
                   type=str,
                   dest='filename1',
                   default="v1.txt",
                   help="array one can be found at [target_directory]/[f1]"\
                    "target_directory defaults to current directory if not set"\
                    "f2 defaults to v2.txt if not set")

parser.add_argument('--f2',
                   action='store',
                   type=str,
                   dest='filename2',
                   default="v2.txt",
                   help="the relevant files can be found at [target_directory]/[f2]"\
                    "target_directory defaults to current directory if not set"\
                    "f2 defaults to v2.txt if not set")

parser.add_argument('--target_directory',
                   action='store',
                   type=str,
                   dest='target_directory',
                   default=os.getcwd() + '/',
                   help="the relevant files can be found at {working_directory}+/+{basename}+*")

parser.add_argument('--op',
                    action='store',
                    type=str,
                    dest='op',
                    default='-',
                    choices=['+','-','dot','vdot'],
                    help="operation to perform between f1 and f2")

parser.add_argument('--datatype',
                    action='store',
                    type=str,
                    dest='datatype_str',
                    default='complex128',
                    choices=['int64','float32', 'float64', 'complex64', 'complex128'],
                    help='datatype of matrix, will default to np.complex128')

args = parser.parse_args(sys.argv[1:])

target_directory = str(args.target_directory)
print("target_directory = ", target_directory)

filepath1 = target_directory+str(args.filename1)
print("filepath1 = ", filepath1)
clean_file(filepath1)

filepath2 = target_directory+str(args.filename2)
print("filepath2 = ", filepath2)
clean_file(filepath2)

op = str(args.op)
print("op = ", op)

datatype = set_datatype(str(args.datatype_str))
print("datatype = ", datatype)
print(type(datatype))

arr_out = manipulate_txt_arrays(filepath1, filepath2, op, datatype)
if op != ("dot" or "vdot"):
    out_name = str(args.filename1).replace('.txt',op) + str(args.filename2)
    out_path = target_directory+out_name
    print("\n output can be found in", out_path)
    np.savetxt(out_path, arr_out)
else:
    print (op + " product = ", arr_out)

print_max = True
print_min = True
if print_max:
    ind = np.unravel_index(np.argmax(arr_out, axis=None), arr_out.shape)
    print("max value at ", ind, " = ", arr_out[ind])
if print_min:
    ind = np.unravel_index(np.argmin(arr_out, axis=None), arr_out.shape)
    print("min value at ", ind, " = ", arr_out[ind])
