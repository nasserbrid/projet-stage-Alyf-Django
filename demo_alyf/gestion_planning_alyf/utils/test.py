

def testfunc():
    dico = {"a":1, "b":2, "c":3}

    deco = iter(dico)

    duco= {}


    for i in range(2):
        key = next(deco)
        duco.update({key:dico[key]})

    print(duco)


testfunc()