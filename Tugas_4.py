mahasiswa = ['Andi', 'Budi', 'Caca', 'Dudi', 'Eca']
uts = [75, 90, 80, 65, 70]
uas = [100, 80, 60, 70, 90]
ratarata=[]
    
print('Nama\t', end=' ')
for nama in mahasiswa:
    print(nama, end='\t')
print()

print('UTS\t',end=' ')
for nilai_uts in uts:
    print(nilai_uts, end='\t')
print()   

print('UAS\t', end=' ')
for nilai_uas in uas:
    print(nilai_uas, end='\t')
print()
       
for i in range(5):
    ratanilai=(uts[i]+uas[i])/2
    ratarata.append(ratanilai)
   
index_tertinggi=ratarata.index(max(ratarata))
index_terendah=ratarata.index(min(ratarata))

print("Nilai tertinggi didapatkan oleh: ",mahasiswa[index_tertinggi], ", dengan rata-rata: ",ratarata[index_tertinggi])
print("Nilai tertinggi didapatkan oleh: ",mahasiswa[index_terendah], ", dengan rata-rata: ",ratarata[index_terendah])