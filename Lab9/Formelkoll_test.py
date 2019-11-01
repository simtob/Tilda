#Martin Neihoff 2019

from subprocess import Popen, PIPE
from sys import argv
from tkinter import filedialog,Tk


def get_hammer_distance(A: str, B: str):
    distance = 0
    error_str = ""
    if len(A) != len(B):
        distance += abs(len(A) - len(B))

    str_length = len(A) if len(A) < len(B) else len(B)
    for i in range(str_length):
        if A[i] != B[i]:
            distance += 1
            error_str += '^'
        else:
            error_str += ' '
    for i in range(str_length, len(error_str)):
        error_str += '^'
    return distance, error_str

def get_subject_name():
    root = Tk()
    root.withdraw()
    file_name = filedialog.askopenfilename()
    valid_name = False
    while not valid_name:
        try:
            open(file_name, 'r')
        except:
            print("Not a valid file")
            file_name = filedialog.askopenfilename()
        else:
            valid_name = True
    return file_name


def test_subject(subject_name):
    test_files_dir = "Labboration9"
    if len(argv) > 2:
        test_files_dir = argv[2]

    try:
        input_file = open("test_input.txt", 'r')
        output_file = open("test_output.txt", 'r')
    except:
        print("Could not open input or output test files.\nOpen the folder where the test files are.")
        files_found = False
        while files_found == False:
            test_files_dir = filedialog.askdirectory()
            try:
                input_file = open(test_files_dir + "/test_input.txt", 'r')
                output_file = open(test_files_dir + "/test_output.txt", 'r')
            except:
                print("Files not found in this directory")
            else:
                files_found = True


    output_data = output_file.readlines()
    input_data = input_file.readlines()

    print("Opening program...")
    process = Popen(['python', subject_name], stdout=PIPE, stderr=PIPE, stdin= PIPE)
    print("Writing to program...")
    for line in input_data:
        print("Input: ", line)
        try:
            process.stdin.write( bytes(line, encoding = "utf-8"))
        except OSError as err:
            print("Could not send input: ", line)
            print("Error: \n", err)
    print("Retreiving output...")

    test_output, errors = process.communicate()
    test_output = str(test_output)
    test_output = test_output[2:]
    test_output = test_output[:-1]
    test_output = test_output.replace("\\n", "\n")
    test_output = test_output.replace("\\r", "")
    test_output = test_output.replace("\\xc4", "ä")
    test_output = test_output.replace("\\xf6", "ö")
    test_output = test_output.split("\n")
    if str(errors, encoding="utf-8") != "":
        print("File raised errors:\n", str(errors, encoding="utf-8").replace("\\n", "\n"))

    line_counter = 0
    error_counter = 0
    error_list = []

    for line in test_output:
        if line_counter >= len(output_data):
            break
        output_data[line_counter] = output_data[line_counter].replace("Ã¤", "ä")
        output_data[line_counter] = output_data[line_counter].replace("Ã¶", "ö")
        if line != output_data[line_counter]:
            hammer_distance, error_str = get_hammer_distance(line, output_data[line_counter])
            if hammer_distance > 1:
                print("**********************************")
                print("Wrong answer at line ", line_counter)
                print("Given input: ", input_data[line_counter].strip())
                print("Received output: ", line.strip())
                print("Expected output: ", output_data[line_counter].strip())
                print("                 ", error_str)
                print("Length difference: ", abs(len(line) - len(output_data[line_counter])))
                print("Hammer distance between answers: ", hammer_distance)
                print("**********************************\n")
                error_counter+=1
            
        line_counter+=1
        if not line_counter%100:
            print("At line ", line_counter, " (Currently ", error_counter, " Errors)")
    
    print("*************************")
    print("Total inputs:", line_counter)
    print("Total number of errors", error_counter)
    input()



def main():
    print(""""Welcome to lab 9 tester!
    Select your solution to test it. Do note that some errors in the output strings might not be detected, but this program should help you find most of you errors.""")
    if len(argv) > 1:
        subject_name = argv[1]
    else:
        subject_name = get_subject_name()
    test_subject(subject_name)
    

    

if __name__ == "__main__":
    main()