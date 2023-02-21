import os

def check_correction(path_to_code, path_to_input, path_to_output):
    os.sys(f"./{path_to_code} < {path_to_input} > temp.txt")

    with open(f"{path_to_input}", 'r') as outfile:
        data = outfile.read()
    
    print(data)

check_correction("./a.out", "input.txt", "test")
