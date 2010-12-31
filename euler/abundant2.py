import abuns
N = 28124
abuns.abuns
sumsofabuns = []
for a, m in enumerate(abuns.abuns):
    for n in abuns.abuns[a:]:
        if m+n < N:
            sumsofabuns.append(m+n)
sumsofabuns = set(sumsofabuns)
negse = [x for x in range(N) if x not in sumsofabuns]

