#  File: DNA.py
#  Student Name: Akwawo Ekpu
#  Student UT EID: ace2453

import sys


# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequences. The list is empty if there are no
#         common subsequences.
def longest_subsequence(s1, s2):
    pass
    longest_seq = 0
    list_seq = []
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            count = 0
            seq = ''
            while (i + count < len(s1)) and (j + count < len(s2)) and s1[i + count].upper() == s2[j + count].upper():
                seq += s1[i + count].upper()
                count += 1
            if count > longest_seq:
                longest_seq = count
                list_seq = [seq]
            elif count == longest_seq and (seq not in list_seq) and   count > 0:
                list_seq.append(seq)
                
    if list_seq:
        return sorted(list_seq)
    else:
        return 0
            

# Input: list of strings, one string per file input line
# Output: process each pair of DNA strings in the list
def process_lines(lines):
    pass
    strand = int(lines[0])
    line_idx = 1

    for i in range(strand):
        s1 = lines[line_idx].strip()
        s2 = lines[line_idx + 1].strip()
        com_seq = longest_subsequence(s1, s2)
        if com_seq:
            print("\n".join(sorted(com_seq)))
        else:
            print("No Common Sequence Found")
            
        print()
        line_idx += 2


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        # in_data = open('autograde/test_cases/test_3.in')
        in_data = open('dna.in')
    else:
        in_data = sys.stdin

    # input will be list of strings, one string per line
    lines = in_data.readlines()

    # process the lines
    process_lines(lines)
    in_data.close()


if __name__ == "__main__":
    main()
