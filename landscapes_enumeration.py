for k in range(4, 19):
    enum_total = 0
    enum_equiv = 0
    u = [0 for x in range(k - 1)] #symbols before and after *
    for s in range(1, (k + 1) // 2): #placement of *
        a = 1
        u[a] = -1
        while a > 0:
            u[a] += 1
            while a > 0 and u[a] == min(3, k - a): #symbols can be 0, 1 or 2(-), but the last one cannot be 2
                a -= 1
                if a > 0:
                    u[a] += 1
            if a > 0:
                if a == k - 2: #all symbols generated
                    mirror = False #property mirror means that u is equal to itself read backwards, possibly with 0 and 1 swapped at each entry
                    acceptable = True #valid solution
                    if 2 * s == k - 1: #check if "mirror", or already counted
                        b = 0
                        while 2 * b < k - 2 and ((u[k - 2] == 0 and u[b] == u[k - 2 - b]) or (u[k - 2] == 1 and u[b] == 2 - ((u[k - 2 - b] + 1) % 3))):
                            b += 1
                        if 2 * b == k - 1:
                            mirror = True
                        else:
                            if (u[b] == 1 and u[k - 2 - b] < 2) or u[b] == 2:
                                acceptable = False
                    b = 0
                    while acceptable and b <= a:
                        if u[b] < 2:
                            if b < s:
                                c = s - b #absolute value of d_1
                            else:
                                c = b + 1 - s
                            d = 0
                            found = False #initially not found d_2 satisfying the condition of Cor 1.9
                            while d <= a - c + 1 and not found:
                                if u[d] < 2 and d + c != s:
                                    e = d + c
                                    if d < s and e > s:
                                        e -= 1
                                    if e <= a and u[e] == 1 - u[d]:
                                        found = True
                                d += 1
                            if not found:
                                acceptable = False
                        b += 1
                    if acceptable:
                        if mirror:
                            enum_total += 2
                        else:
                            enum_total += 4
                        enum_equiv += 1
                else:
                    a += 1
                    u[a] = -1
    print(k, enum_total, enum_equiv)