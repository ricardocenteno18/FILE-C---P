# firt i make a list of numbers to print in the file .txt
num = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', '...']
#Then i call the file .txt and connect with a pointer
write_ptr = 'wrt.txt'
fichero = open(write_ptr, 'w')
for l in num:
#make the opeation to write 
    fichero.write(l + '\n')
#close the pointer and the file .txt
fichero.close()