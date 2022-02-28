# python 
import hashlib as hasher 
o = open("key.txt","w")
o.write("helnsnnzjzjznnzbxbbxbbxbxnxnnxnxnxnxnnxmxmxmxmxnndndndnndndnndndndnnsnsnsnznkskslzkzjndndndjdjzmnznsjksksllsksjsmsksksk")
o.close()
print(""" 
[+]sha512 ile dosya şifreleme
[+]sha3_512 ile dosya şifreleme 
[+]sha3_384 ile dosya şifreleme 
[+]sha3_256 ile dosya şifreleme
[+]sha3_224 ile dosya şifreleme
[+]sha384 ile dosya şifreleme
[+]sha256 ile dosya şifreleme
[+]sha224 ile dosya şifreleme
[+]sha1 ile dosya şifreleme

bu tool dosyadaki verileri şifreler 
geri alınmaz onun için iyi düşünün 
Bu toopda sorumluluk kabul kâtiyen etmiyorum!!
örnek dosya için key.txt yazabilirsiniz. 
key.txt dosyanız varsa silinit!!""")
print("-"*30)
print("""
kod yazarı: SpyGoldEye 
codes by : SpyGoldEye 
""")
print("-"*30)

try:
    secim = int(input("Seçiminizi giriniz: "))
except:
    raise ValueError("Lütfen sayı giriniz ve verilen rakamları kullanınız")
    

    
def m1():
    try:
        gir = input("şifrenelecek dosya: ")
        yaz3 = open(gir,'r+')
        hash3 = hasher. sha512()
        ha3 = hash3.hexdigest()
        yaz3.write(ha3)
    except:
        print("Hata oldu kusura bakmayın ")
    finally:
        yaz3.close()
    
def m2():
    try:
        gir = input("şifrenelecek dosya: ")
        yaz4 = open(gir,'r+')
        hash4 = hasher.sha3_512()
        ha4 = hash4.hexdigest()
        yaz4.write(ha4)    
    except:
        print("Hata !!! tekrar deneyin")
    finally:
        yaz4.close()
    
    
def m3():
    
    gir = input("şifrenelecek dosya: ")
    yaz5 = open(gir,'r+')
    hash5 = hasher.sha3_384()
    ha5 = hash5.hexdigest()
    yaz5.write(ha5)
    yaz5.close()
  
    
        
 
 
def m4():
    try:
        gir = input("şifrenelecek dosya: ")
        yaz6 = open(gir,'r+')
        hash6 = hasher.sha3_256()
        ha6 = hash6.hexdigest()
        yaz6.write(ha6)
    except:
        print("Hata oldu sorun var !!")
    finally:
        yaz6.close()

def m5():
    try:
        gir = input("şifrenelecek dosya: ")
        yaz7 = open(gir,'r+')
        hash7 = hasher.sha3_224()
        ha7 = hash7.hexdigest()
        yaz7.write(ha7)
    except:
        print("hata , sorry error")
    finally:
        yaz7.close()
    
def m6():
    
    gir= input("şifrenelecek dosya: ")
    yaz8 = open(gir,'r+')
    hash8 = hasher.sha384()
    ha8 = hash8.hexdigest()
    yaz8.write(ha8)
    yaz8.close()
    
    
def m7():
    try:
        gir = input("şifrenelecek dosya: ")
        yaz9 = open(gir,'r+')
        hash9 = hasher.sha256()
        ha9 = hash9.hexdigest()
        yaz9.write(ha9)        
    except:
        print("Hata ile karşılaştık !! sorry")
    finally:
        yaz9.close()
        
    
def m8():
    try:
        gir = input("şifrenelecek dosya: ")
        yaz_10 = open(gir,'r+')
        hash_10 = hasher.sha224()
        ha_10 = hash_10.hexdigest()
        yaz_10.write(ha_10)
    except:
        print("Bir hata ile karşılaştık Sorry!")
    finally:
        yaz_10.close()
        
   
       
def m9():
    try:
        gir = input("şifrenelecek dosya: ")
        yaz11 = open(gir,'r+')
        hash11 = hasher.sha1()
        ha11 = hash11.hexdigest()
        yaz11.write(ha11)
    except:
        print("Hata oldu kusura bakmayın")
    finally:
        yaz11.close()
        
       
    
if secim == 1:
    m1()
elif secim == 2:
    m2()
elif secim == 3:
    m3() 
elif secim == 4:
    m4()
elif secim == 5:
    m5() 
elif secim == 6:
    m6()
elif secim == 7:
    m7()
elif secim == 8:
    m8()
elif secim == 9:
    m9()
else:
    print("Lütfen Seçim yukardaki gibi giriniz!!!")
