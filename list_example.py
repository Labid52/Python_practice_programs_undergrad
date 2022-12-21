filerf = open('D:\media-files\certificate-knb-ndonesia\ITB\itb-resident.txt', 'r')
#lines  = filerf.readlines()
for lin in filerf:
    print(lin.strip())
#print(lines[:4])
filerf.close()