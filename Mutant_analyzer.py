import pandas as pd
import matplotlib.pyplot as plt
from Bio.Seq import Seq

print("Mutation Impact Analyzer")

# Take DNA sequences 
original_dna = input("Enter original DNA sequence: ").upper()
mutated_dna = input("Enter mutated DNA sequence: ").upper()

# Check if both sequences are same length
if len(original_dna) != len(mutated_dna):
    print("DNA sequences must be of same length")
    exit()

print("Codon Change | Amino Acid Change | Mutation Type")
print("-----------------------------------------------")

# Initialize counters
silent_count = 0
missense_count = 0
nonsense_count = 0

# Read DNA in codons
for i in range(0, len(original_dna), 3):

    original_codon = original_dna[i:i+3]
    mutated_codon = mutated_dna[i:i+3]

    if len(original_codon) < 3 or len(mutated_codon) < 3:
        continue

    if original_codon != mutated_codon:

        original_aa = Seq(original_codon).translate()
        mutated_aa = Seq(mutated_codon).translate()

        if original_aa == mutated_aa:
            mutation = "Silent mutation"
            silent_count += 1
        elif mutated_aa == "*":
            mutation = "Nonsense mutation"
            nonsense_count += 1
        else:
            mutation = "Missense mutation"
            missense_count += 1

        print(original_codon, "->", mutated_codon, "|",
              original_aa, "->", mutated_aa, "|", mutation)

print("Analysis finished")

# Visualization
data = {
    "Mutation Type": ["Silent", "Missense", "Nonsense"],
    "Count": [silent_count, missense_count, nonsense_count]
}

df = pd.DataFrame(data)
df
plt.bar(df["Mutation Type"], df["Count"])
plt.xlabel("Mutation Type")
plt.ylabel("Number of Mutations")
plt.title("Mutation Impact on Protein")
plt.show()
