#!/usr/bin/env python

##### this python script is saved under pycommand inside immdbg directory
##### this script can be run along side with immdbg to automate debugging binary tasks
##### and print out useful results for analysis at a later time


# importing necessary modules

import immlib		# this lib is shipped with the immunity framework


DESC = "this script will output current process data to a csv file name procInfo_output.csv in the immunity debugger directory"

def main(args):
    # starting the debugger instance
    imm = immlib.Debugger()
    filename = "procInfo_output.csv"

    reset_file(filename)                            # for this particular task, we should reset the file every time the program is run
                                                    # this way we dont get repeated processes' info printed on the output file
    head_row = "PID,name,Path,Services"
    append_row(filename, head_row)

    # grabbing data from pocess list
    psList = imm.ps()

    # appending each of the process data to the ouput file
    for process in psList:   
        append_row(filename, str(process[0]) + "," + process[1] + "," + process[2] + "," + str(process[3]))

    # log back to the status box upon completion
    return "[!] spse-procInfo_csvOuput is finished with status 0"

def reset_file(filename):
    # this is where we can set a brand new outputfile, we can even timestamp it
    f = open(filename, "w")
    f.write("\n")
    # time stamp etc
    f.close()

def append_row(filename, data):
    # open file, and append to it
    f = open(filename, "a")

    # writing the input data to the file and adding a new line
    f.write(data + '\n')

    # closing the file
    f.close()

