def header(title):
    print("-" * 50)
    print("\t\t", title)
    print("-" * 50)

def ubahRamKeMbps(ramInGbps):
    return ramInGbps * 1024

def hitungSO(ram, so):
    return ram / so