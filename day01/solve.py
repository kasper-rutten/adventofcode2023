import regex as re # third party regex supports overlapping matches

def find_first_and_last_re(line):
    numbers_regex = '[0-9]|one|two|three|four|five|six|seven|eight|nine'
    all_numbers = re.findall(numbers_regex,line, overlapped=True)
    #print(f"found numbers: {all_numbers} in line {line[:-1]}, returning {[all_numbers[0], all_numbers[-1]]}")
    return([all_numbers[0], all_numbers[-1]])

def substitute_number_strings_with_numbers(array):
    to_be_substituted = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    output_str = "".join(array)
    for i in range(0, 10):
        #print(f"attempting to substitute {to_be_substituted[i]} for {str(i)} in line {substitute}")
        output_str = output_str.replace(to_be_substituted[i], str(i))
    return output_str

with open('input') as f:
    lines = f.readlines()
    first_and_last_array = []
    sum_of_all_firsts_and_lasts = 0
    for line in lines:
        first_and_last_array = find_first_and_last_re(line)
        first_and_last_array = substitute_number_strings_with_numbers(first_and_last_array)
        first_and_last_number_numeric = int(first_and_last_array)
        sum_of_all_firsts_and_lasts += first_and_last_number_numeric
        #print(f"At line {index} - {line}, adding {first_and_last_number_numeric} to rolling sum {sum_of_all_firsts_and_lasts}")
    print(sum_of_all_firsts_and_lasts)
