import numpy as np
import argparse
import sys
import os

def manipulate_txt_arrays(filename1, filename2, op, data_type):
    arr1 = np.loadtxt(filename1, data_type)
    arr2 = np.loadtxt(filename2, data_type)
    np.savetxt(filename1 + "_out", arr1)
    np.savetxt(filename2 + "_out", arr2)
    print("===== arr1 =====\n", arr1)
    print("===== arr2 =====\n", arr2)

usage = 'manipulate_arrays --f1=filename1  --f2=filename2 --op=+,-,dot  (will do f1 op f2)'

parser = argparse.ArgumentParser( usage, formatter_class=argparse.ArgumentDefaultsHelpFormatter )

parser.add_argument('--basename',
                   action='store',
                   type=str,
                   dest='basename',
                   default=None,
                   help="the relevant files can be found at {target_directory}+/+{basename}+*"\
                    "target_directory defaults to current directory if not set")

parser.add_argument('--target_directory',
                   action='store',
                   type=str,
                   dest='target_directory',
                   default=os.getcwd() + '/',
                   help="the relevant files can be found at {working_directory}+/+{basename}+*")


args = parser.parse_args(sys.argv[1:])
filename1 = "v1.txt"
filename2 = "v2.txt"
op = "+"
basename = str(args.target_directory)+str(args.basename)
print("filename1 = ", filename1)
print("filename2 = ", filename2)
manipulate_txt_arrays(filename1, filename2, op, np.complex128)
