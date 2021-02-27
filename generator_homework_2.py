from Bio.Seq import Seq

def translation(path, codon_table="Standard"):
    with open(path, 'r') as fasta:
        text = [line.rstrip("\n") for line in fasta]
    seq = text[1::2]
    for i in range(len(seq)):
        yield Seq(seq[i]).translate(table=codon_table)


fasta_path = "C:/Users/maxim/Desktop/диплом(вопрос)/fasta_1.fa"
protein = translation(fasta_path, codon_table="Standard")
print(next(protein))


