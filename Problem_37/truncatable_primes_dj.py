from primes import primes


def truncate(n, dir):
    '''returns a list of values of n truncated from left or right (depending on dir)'''
    out = []
    s = str(n)
    if dir == "right":
        for i in range(len(s)):
            out.append(s[i:])
    elif dir == "left":
        for i in range(len(s)):
            out.append(s[:i + 1])
    else:
        raise ValueError("dir must be 'left' or 'right'")

    out = [int(i) for i in out]
    return out


ps = primes(10000000)
ps_set = set(ps)

truncatable = []
i = 0
while len(truncatable) < 11:
    p = ps[i]
    if p < 10:
        i += 1
        continue
    #    print(p)
    tl = truncate(p, "left")
    tr = truncate(p, "right")
    #    print(tl)
    #    print(tr)
    if (set(tl).issubset(ps_set) and set(tr).issubset(ps_set)):
        truncatable.append(p)
        print(p)
    i += 1

print(truncatable)
print(sum(truncatable))
