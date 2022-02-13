jumlah_baju=int(input("masukkan jumlah baju yang di beli:"))    
for i in range (jumlah_baju):
    nama_baju=input("masukkan nama baju:")
    harga_baju=int(input("masukkan harga baju: Rp."))
    nilai=[]
if jumlah_baju >= 3:
        nilai.append(harga_baju)
        total_pembelian=sum(nilai)
        kena_ppn=(2/100*total_pembelian)
        potongan_harga=(total_pembelian + kena_ppn)*10/100
        total_pembelian_bersih=total_pembelian-potongan_harga
        print("total harga yang di bayar setelah diskon",total_pembelian_bersih)
        print("anda mendapatkan bonus baju ")
elif jumlah_baju <3:
        nilai.append(harga_baju)
        total_pembelian=sum(nilai)
        kena_ppn=(2/100*total_pembelian)
        total_pembelian_bersih=total_pembelian+kena_ppn
        print("jumlah total harga yang harus di bayar:",total_pembelian_bersih)
        print("maaf anda tidak dapat bonus")
        
