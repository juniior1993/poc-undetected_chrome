from hapaglloydhandle import HapagLloydHandle


if __name__ == '__main__':

    bls = ['HLCUBSC2207BGZM61','HLCUME3220850257','HLCUME3220855685','HLCUME3220809417','HLCUME3220845645','HLCUTPE220761980','HLCUJK1220804826','HLCUBSC2207BFRL3']

    hapaglloydhandle = HapagLloydHandle('files/')
    for bl in bls:
        hapaglloydhandle.handle(bl)