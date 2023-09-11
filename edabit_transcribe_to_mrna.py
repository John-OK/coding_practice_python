def dna_to_rna(dna):
    mrna = ""
    dna_base_complements = {"A": "U", "T": "A", "G": "C", "C": "G"}

    for base in dna:
        mrna += dna_base_complements[base]

    return mrna

print(dna_to_rna("GATTACA")) # >> "CUAAUGU"