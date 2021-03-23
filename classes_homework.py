import re


class RNA:
    def __init__(self, seq):
        for i in seq:
            if i not in ['A', 'U', 'C', 'G']:
                raise ValueError
        self.seq = seq
        self.index = -1

    def __repr__(self):
        return self.seq

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.seq):
            self.index = -1
            raise StopIteration
        else:
            return self.seq[self.index]

    def __eq__(self, other) -> bool:
        return isinstance(other, RNA) and (self.seq == other.seq)

    def __hash__(self) -> int:
        return hash(self.seq)

    def gc_content(self):
        return (self.seq.count('G') + self.seq.count('C')) / len(self.seq) * 100

    def reverse_complement(self):
        reverse = self.seq.replace('G', 'c').replace('C', 'g').replace('A', 'u').replace('U', 'a')
        return reverse[::-1].upper()


class DNA:
    def __init__(self, seq):
        for i in seq:
            if i not in ['A', 'T', 'C', 'G']:
                raise ValueError
        self.seq = seq
        self._index = -1

    def __repr__(self):
        return self.seq

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self.seq):
            self._index = -1
            raise StopIteration
        else:
            return self.seq[self._index]

    def __eq__(self, other) -> bool:
        return isinstance(other, DNA) and (self.seq == other.seq)

    def __hash__(self) -> int:
        return hash(self.seq)

    def gc_content(self):
        return (self.seq.count('G') + self.seq.count('C')) / len(self.seq) * 100

    def reverse_complement(self):
        reverse = self.seq.replace('G', 'c').replace('C', 'g').replace('A', 't').replace('T', 'a')
        return reverse[::-1].upper()

    def transcribe(self):
        mRNA = self.seq.replace('G', 'c').replace('C', 'g').replace('A', 'u').replace('T', 'a')
        return RNA(seq=mRNA.upper())

seq_1 = DNA('TGTTGGGGAATCATGC')
seq_2 = DNA('TGTTGGGGAATCATGC')
seq_3 = DNA('TGTTGGGGAATCAGC')
print(seq_1.gc_content())
print(seq_1.reverse_complement())
print(seq_1.transcribe())
for i in seq_1:
    print(i)
print(seq_1 == seq_2)
print(seq_1 == seq_3)

seq_4 = RNA('UUUUAAAAAAGCGCGCG')
seq_5 = RNA('UUUUAAAAAAGCGCGCG')
seq_6 = RNA('UUUUAAAGCGCGCG')
print(seq_4.gc_content())
print(seq_4.reverse_complement())
for i in seq_4:
    print(i)
print(seq_4 == seq_5)
print(seq_4 == seq_6)