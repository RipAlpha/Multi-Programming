#NAMA KELOMPOK
#5200411450 RETNO PRIHATINI
#5200411122 GRESSENSIA OLIVIA NENO A
#5200411343 PANDU TEJA S
#5200411347 MUHAMMAD SYARIFUDIN

import helper

helper.header("Multiprogramming")

totalRam = int(input("Masukkan Kapasitas RAM: "))
totalSO = int(input("Masukkan Kapasitas Sistem Operasi: "))
Multip = helper.hitungSO(helper.ubahRamKeMbps(totalRam), totalSO)

print("Kapasitas Sistem Operasi adalah ", Multip , "KB per blok" )
print("\n<-- Eksekusi Program -->")


ramUntukProgram1 = int(input("Kapasitas Program 1 : "))
ramUntukProgram2 = int(input("Kapasitas Program 2 : "))
ramUntukProgram3 = int(input("Kapasitas Program 3 : "))
Kaprog1 = helper.hitungSO(helper.ubahRamKeMbps(ramUntukProgram1), Multip)
Kaprog2 = helper.hitungSO(helper.ubahRamKeMbps(ramUntukProgram2), Multip)
Kaprog3 = helper.hitungSO(helper.ubahRamKeMbps(ramUntukProgram3), Multip)


print("\nInformasi Multiprogramming")
print("-"*60)

print("Total Kapasitas RAM = ", totalRam)
print("\nTotal Kapasitas Sistem Operasi = ", totalSO)
print("\nKapasitas Terpakai = ", Kaprog1 + Kaprog2 + Kaprog3)
print("\nTotal Kapasitas Program = ",totalSO + Kaprog1 + Kaprog2 + Kaprog3)
print("\nKapasitas SO yang tidak terpakai = ", totalSO - (Kaprog1 + Kaprog2 + Kaprog3))