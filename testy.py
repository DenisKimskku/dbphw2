###TESTER for 1-1 and 1-2 checking result ####


def compare_result(file_dir_list, pareto_output=None):
    skylines = []

    # Read thje data from each file and store them in skylines
    for file in file_dir_list:
        with open(file, 'r') as f:
            lines = f.readlines()
            lines = set(tuple(line.strip().split()) for line in lines)
            skylines.append(lines)

    # If pareto_output is provided, add it to skylines
    # Check if all skyline results are identical to confirm Pareto Optimality.    
    if pareto_output:
        skylines.append(set(tuple(line) for line in pareto_output))
        if all(x == skylines[0] for x in skylines):
            print('Pareto Correct!')
        else:
            print('Pareto Incorrect!')

    # If more than one files are provided, check if all outputs are identical.
    if len(file_dir_list) > 1:
        if all(x == skylines[0] for x in skylines):
            print('Same output:)')
        else:
            print('Different output:(')

file_dir_list = ['./output/p1_1.txt', './output/p1_2.txt']
compare_result(file_dir_list)
