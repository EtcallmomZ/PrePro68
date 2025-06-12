"""actors"""
def oh_yi_young():
    """oh"""
    print('Go Youn-jung')

def pyo_nam_kyung():
    """pyo"""
    print('Shin Si-ah')

def kim_sa_bi():
    """kim"""
    print('Han Ye-ji')

def um_jae_il():
    """um"""
    print('Kang You-seok')

def main():
    """main"""
    actor = input()
    if actor == "yiyoung" :
        oh_yi_young()
    elif actor == "namkyung":
        pyo_nam_kyung()
    elif actor == "sabi":
        kim_sa_bi()
    elif actor == "jaeil":
        um_jae_il()
    else:
        print("No actor matched")

main()
