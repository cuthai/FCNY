import filecmp

file1 = 'h:\\desktop\\2018_6_21_IHAFCNY_Medical_Claims_20180609.txt.txt'
file2 = 'h:\\desktop\\2018_3_7_IHAFCNY_Medical_Claims_20180301.txt.txt'

print(filecmp.cmp(file1, file2))