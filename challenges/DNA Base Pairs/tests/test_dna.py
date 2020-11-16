import unittest

from dna import to_comp


class DnaTranscriptionTest(unittest.TestCase):
    def test_empty_rna_sequence(self):
        self.assertEqual(to_comp(""), "")

    def test_dna_complement_of_cytosine_is_guanine(self):
        self.assertEqual(to_comp("C"), "G")

    def test_dna_complement_of_guanine_is_cytosine(self):
        self.assertEqual(to_comp("G"), "C")

    def test_dna_complement_of_thymine_is_adenine(self):
        self.assertEqual(to_comp("T"), "A")

    def test_dna_complement_of_adenine_is_thymine(self):
        self.assertEqual(to_comp("A"), "T")

    def test_rna_complement(self):
        self.assertEqual(to_comp("ACGTGGTCTTAA"), "TGCACCAGAATT")
