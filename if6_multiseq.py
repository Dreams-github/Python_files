s="""CTTTGTACAAGAAAGCTGGGCGGCCGCTTTTTTTTTTTTTTTTTTTTTTTACTTAAGCAGTCTTTAATGA
AAGCCGTGCACGAGATGTCTCTACTCCTGCATCTTCTCGATCGTTTCTTCCTTGTATTTGCCCTTCTCCT
TTCCTACTTGTCGGGACTTGGCTTTCCTCTCCAGGATCTTCTTGCGGTCCTTGTCCAGCTTTAGCCTGGT
GATAACGACCTTGCTGGGGTGGATGCCCACATGGACGGTTGTGCCATTAGCCTTCTCTCGCTGGACTCGT
TCGATGTAGATGACGTACTTCTTCCTGTACACTTGGACCACCTTGCCAATCTGCTGGCCTTTGTAGTGTC
CGCGAACAACCTGAACTTCGTCATCCTTCCGAATGGGCATAGACCGAACGTTATACGAAGAGCCTGCTTT
TTTGTACAAACTTGTGAAAGCTTCAGCTGCTCGAGGGGGGGCCCGGTACCCAATTCGCCCTATAGTGAGT
CGTATTACGCGCGCTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACT
TAATCGCCTTTGCAGAAATT"""
print(s)
print(len(s))

ss=s.replace("\n","")
print(ss)
print(len(ss))

pattern="CTT"

if(pattern in ss):
    print("pattern is present",pattern)
    c=s.count(pattern)
    print("count of CTT",c)
    per=(c/len(ss))*100
    print("percentage",per)

else:
    print("pattern is not present")