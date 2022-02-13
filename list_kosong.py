#membuat list kosong untuk menampung warna

warna = []
stop = False
i = 0

while(not stop):
    warna_baru = raw_input("Inputkan hobi yang ke-{}: ".format(i))
    hobi.append(warna_baru)

    i += 1
    
    tanya = raw_input("Mau isi lagi? (y/t): ")
    if(tanya == "t"): 
        stop = True

print("Kamu memiliki {} hobi".format(len(hobi))

