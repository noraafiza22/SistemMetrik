# Procedure menu

def menu():
    print("***************************************")
    print("Sistem Metrik")
    print("1. Berat / Mass")
    print("2. Jarak / Distance")
    print("3. Isipadu cecair / Volume of liquid")
    print("4. Suhu / Temperature") 
    print("5. Tamat")
    print("***************************************")
 
# Function dapat pilihan pengguna
def pilihanPengguna():
    noPilihan = 0
    while (noPilihan <1 ) or (noPilihan >5):
        noPilihan = int(input("Pilihan anda [1 hingga 5]:"))
    return noPilihan

# Function dapatkan nombor
def dptNombor():
    nombor = int(input("Masukkan nombor: "))
    return nombor

# Procedure kira
def kira(pilihan, nombor):
    if pilihan == 1:
        print("\nOutput : "+ str(nombor)+ " gram = " + str(nombor / 1000)+" kilogram")
        print("Output : "+ str(nombor)+ " gram = " + str(nombor *1000)+" miligram")
        print("***************************************")
    
    elif pilihan == 2:
        print("\nOutput : "+ str(nombor)+ " meter = " + str(nombor / 1000)+" kilometer")
        print("Output : "+ str(nombor)+ " meter= " + str(nombor * 100)+" centimeter")
        print("Output : "+ str(nombor)+ " meter = " + str(nombor * 1000)+" milimeter")
        print("***************************************")   
    
    elif pilihan == 3:
        print("\nOutput : "+ str(nombor)+ " liter =" + str(nombor * 1000)+" mililiter")
        print("***************************************")
    
    elif pilihan == 4:
        print("\nOutput : "+ str(nombor)+ " celcius = " + str(nombor * 33.8)+" fahrenheit")
        print("Output : "+ str(nombor)+ " celcius= " + str(nombor * 274.15)+" kelvin")
        print("***************************************")

# main
flag = 1
while flag == 1:
    menu()
    jenisOperasi = pilihanPengguna()
    if jenisOperasi == 5:
        flag = 0
    else:
        nombor= dptNombor()
        kira(jenisOperasi,nombor)
print("Terima Kasih")
