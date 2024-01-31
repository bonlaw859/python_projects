#set constants
MIN_CODON = 5
CG_PERCENT = 30
UNIQUE_NUC = 4
NUC_P_CODON = 3

#define main
def main():

    #print intro
    print("This program reports information about DNA")
    print("nucleotide sequences that may encode proteins.")

    #get file names from user
    input_f = input("Input file name? ")
    output_f = input("Output file name? ")

    #open files
    with open(input_f, 'r') as input_file, open(output_f, 'w') as output_file:
        lines = input_file.readlines()

        #set loop to read all lines
        for i in range(0, len(lines), 2):
            #get region name from first line
            region_name = lines[i].strip()
            #get nucleotide sequence from second line
            nuc = lines[i+1].strip().upper()
            #call function to count nucleotide occurances
            nuc_count = count_nuc(nuc)
            #set variables from function that computes mass
            mass_perc, total_mass, c_perc, g_perc = compute_mass_perc(nuc_count)
            #get list of codons
            codons_list = extract_codons(nuc)
            #determine if protein
            is_protein_gene = "YES" if is_protein(nuc, c_perc, g_perc) else "NO"

            #write output file
            output_file.write(f"Region Name: {region_name}\n")
            output_file.write(f"Nucleotides: {nuc}\n")
            output_file.write(f"Nuc. Counts: {nuc_count[:UNIQUE_NUC]}\n")
            output_file.write(f"Total Mass%: {mass_perc} of {total_mass}\n")
            output_file.write(f"Codons List: {codons_list}\n")
            output_file.write(f"Is Protein?: {is_protein_gene}\n\n")

#function that computes mass percentage of nucleotides and junk
def compute_mass_perc(nuc_count):

    #compute mass of each item based on count
    a_mass = (nuc_count[0] * 135.128)
    c_mass = (nuc_count[1] * 111.103)
    g_mass = (nuc_count[2] * 151.128)
    t_mass = (nuc_count[3] * 125.107)
    j_mass = (nuc_count[4] * 100.000)

    #get total mass
    total_mass = a_mass + c_mass + g_mass + t_mass + j_mass

    #calculate percentage of mass of each item
    a_perc = round(((a_mass / total_mass) * 100), 1)
    c_perc = round(((c_mass / total_mass) * 100), 1)
    g_perc = round(((g_mass / total_mass) * 100), 1)
    t_perc = round(((t_mass / total_mass) * 100), 1)
    j_perc = round(((j_mass / total_mass) * 100), 1)

    #return list of percents, total mass, and c + g percentages
    return ([a_perc, c_perc, g_perc, t_perc],
            round(total_mass, 1), c_perc, g_perc)

#function that counts the occurances of nucleotides and junk
def count_nuc(sequence):

    #set list based on unique nucleotides constant
    nuc_count = [0] * (UNIQUE_NUC + 1)

    #loop to count each item based on index of list
    for char in sequence:
        if char == 'A':
            nuc_count[0] += 1
        elif char == 'C':
            nuc_count[1] += 1
        elif char == 'G':
            nuc_count[2] += 1
        elif char == 'T':
            nuc_count[3] += 1
        elif char == '-':
            nuc_count[4] += 1

    #return count of items
    return nuc_count

#function to create list of codons
def extract_codons(sequence):

    #uppercase the sequence    
    sequence = sequence.upper()
    #set empty list
    codons = []
    #set empty string
    current_codon = ""

    #loop to skip over junk
    for char in sequence:
        #if not junk, add char to current string
        if char != "-":
            current_codon += char
            #once string reaches the nucleotide per codon constant,
            #add to list and reset string
            if len(current_codon) == NUC_P_CODON:
                codons.append(current_codon)
                current_codon = ""
    #return list
    return codons

#function to determine if the sequence represents a protein
def is_protein(sequence, c_perc, g_perc):

    #define start and stop codons
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    #return true if sequencs has start, stop codons, is minimum codons long,
    #and c + g percent meets cg percent constant.
    return (
        sequence.startswith(start_codon) and
        sequence.endswith(tuple(stop_codons)) and
        len(extract_codons(sequence)) >= MIN_CODON and
        c_perc + g_perc >= CG_PERCENT
    )

#call main
main()
