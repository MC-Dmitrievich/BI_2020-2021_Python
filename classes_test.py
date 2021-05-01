import unittest
from classes_homework import DNA, RNA


class RNA_Test(unittest.TestCase):

    def test_rna_is_string(self):
        rna = RNA('AAUUGGCC')
        self.assertTrue(isinstance(rna.seq, str))

    def test_rna_raises_error_if_seq_is_empty(self):
        with self.assertRaises(ValueError):
            RNA('')

    def test_error_if_rna_is_not_a_string(self):
        with self.assertRaises(TypeError):
            RNA(239)

    def test_rna_oonsists_correct_bases(self):
        rna = RNA('AAUUGGCC')
        self.assertTrue(base in ['A', 'U', 'G', 'C'] for base in rna.seq)

    def test_rna_raises_error_if_seq_consists_of_nonexistent_bases(self):
        with self.assertRaises(ValueError):
            RNA('XXXX')

    def test_rna_has_correct_seq_field(self):
        rna = RNA('AAUUGGCC')
        self.assertEqual('AAUUGGCC', rna.seq)

    def test_rna_are_comparable(self):
        self.assertEqual(RNA('AAUUGGCC'), RNA('AAUUGGCC'))


class DNA_Test(unittest.TestCase):

    def test_dna_is_string(self):
        dna = DNA('AATTGGCC')
        self.assertTrue(isinstance(dna.seq, str))

    def test_dna_raises_error_if_seq_is_empty(self):
        with self.assertRaises(ValueError):
            DNA('')

    def test_error_if_dna_is_not_a_string(self):
        with self.assertRaises(TypeError):
            DNA(239)

    def test_dna_oonsists_correct_bases(self):
        dna = DNA('AATTGGCC')
        self.assertTrue(base in ['A', 'T', 'G', 'C'] for base in dna.seq)

    def test_dna_raises_error_if_seq_consists_of_nonexistent_bases(self):
        with self.assertRaises(ValueError):
            DNA('YYYY')

    def test_dna_has_correct_seq_field(self):
        dna = DNA('AATTGGCC')
        self.assertEqual('AATTGGCC', dna.seq)

    def test_dna_are_comparable(self):
        self.assertEqual(DNA('AATTGGCC'), DNA('AATTGGCC'))


if __name__ == '__main__':
    unittest.main()
