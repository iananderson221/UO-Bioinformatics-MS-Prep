def read_file(file_path):
#Read a file and return a list of lines without newline characters
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def gc_content(DNA_string):
#Calculate GC content as a percentage of the total sequence length
    return round(sum(1 for base in DNA_string if base in "GC") / len(DNA_string) * 100, 6)

def parse_fasta(fasta_lines):
#Convert FASTA-formatted lines into a dictionary of sequences
    fasta_dict = {}
    label = None

    for line in fasta_lines:
        if line.startswith(">"):
            label = line[1:]  # Remove ">" for clarity
            fasta_dict[label] = ""
        else:
            fasta_dict[label] += line  # Append sequence data

    return fasta_dict

#Read the FASTA file
fasta_lines = read_file("rosalind_gc.txt")
fasta_dict = parse_fasta(fasta_lines)

#Compute GC content for each sequence
gc_dict = {label: gc_content(DNA_string) for label, DNA_string in fasta_dict.items()}

#Find the label with the highest GC content
max_gc_label = max(gc_dict, key=gc_dict.get)

#Print result in Rosalind format
print(f"{max_gc_label}\n{gc_dict[max_gc_label]}")
