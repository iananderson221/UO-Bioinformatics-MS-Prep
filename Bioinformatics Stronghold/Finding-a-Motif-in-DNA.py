s = "GATATATGCATATACTT"
t = "ATAT"

for nt in range(len(s)):
    if s[nt:].startswith(t):
        print(nt + 1)
