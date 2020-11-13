def print01(truthtable):
    for tv in truthtable:
        if(tv):
            print("1", end="  ")
        else:
            print("0", end="  ")
    print("")
    return


def truthtable2(s):
    w = 'q  r  '+s
    print(w)
    truth = {True, False}
    for q in truth:
        for r in truth:
            f = eval(s)
            t = [q, r]+[f]
            print01(t)
    return


s = '(not(q&r))==((not q)|(not r))'
truthtable2(s)
