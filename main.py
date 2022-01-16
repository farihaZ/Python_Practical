def main():
    
    # header for the tables
    header =['Dia   ', ' Hora','CO2(ppm)','Temp','humitat relativa','Nom profesor/a','Assignatura']
    header1 =['Sistemes de Ventilació','Temps que roman obert/tencat (min)']
    
    # declaration of the lists
    llist =list()
    hora=list()
    co2llist= list()
    templlist= list()
    humetatllist= list()
    
    
    curso= input("Introdueix el curso :") 
    clas= input("Introdueix el clase :")
    alum=int(input("No. de estuiantes : "))
    while alum < 0 or alum > 25:
        alum=int(input("No. de estuiantes no pueden menor que 0 y meyor que 25 : "))
    
    prof= int(input("Numero de profesores :"))
    while prof < 0 :
        prof= int(input("Numero de profesores :"))
        
    dia=input("Dia en formato DD/MM/AA:")
    dur=input("Duracion  :")
    # the function for inserting the values at diferent times 
    for i in range(7):
            hora.append(input("Time : "))
            
            #the validation of CO2 level that should not be smaller than 0
            co2 = int(input("CO2(ppm) : "))
            while co2 < 0 :
                co2 = int(input("CO2(ppm) : "))
            llist.append(co2)
            co2llist.append(co2)
            
            #validation of the temperature
            temp = int (input("Temperatura : "))
            while temp < -20 or temp > 50 :
                temp = int (input("Temperatura should be between -20 and 50 : "))
            llist.append(temp)
            templlist.append(temp)
           
            #humetat.append(input("Humitat Relativa : "))
            humetat = float(input("Humetat relativa :"))
            while humetat < 0 or humetat > 100 :
                humetat = float(input("Humetat relativa :"))
            llist.append(humetat)
            humetatllist.append(humetat)
    
    nom_p=input("Profesor/a : ")
    assig=input("Assignatura : ")
    
    principal_obr=int(input("Quants min porta principal oberta:"))
    while principal_obr<0:
        principal_obr=int(input("Quants min porta principal oberta:"))
    
    principal_ten=int(input("Quants min porta principal tencada:"))
    while principal_ten <0:
        principal_ten=int(input("Quants min porta principal tencada:"))
    
    segun_obr=int(input("Quants min porta segundaria oberta:"))
    while segun_obr <0:
        segun_obr=int(input("Quants min porta segundaria oberta:"))
    
    segun_ten=int(input("Quants min porta segundaria tencada:"))
    while segun_ten <0:
        segun_ten=int(input("Quants min porta segundaria tencada:"))
    
    fin_ex_obr=int(input("Quants min finestres externes oberta:"))
    while fin_ex_obr < 0:
        fin_ex_obr=int(input("Quants min finestres externes oberta:"))
        
    fin_ex_ten=int(input("Quants min finestres externes tencada:"))
    while fin_ex_ten < 0:
        fin_ex_ten=int(input("Quants min finestres externes tencada:"))
        
    fin_in_obr=int(input("Quants min finestres internes oberta:"))
    while fin_in_obr <0:
        fin_in_obr=int(input("Quants min finestres internes oberta:"))
        
    fin_in_ten=int(input("Quants min finestres internes tencada:"))
    while fin_in_ten <0:
        fin_in_ten=int(input("Quants min finestres internes tencada:"))
        
        
    print("\n")
    # the menu for the cross ventilation 
    print("****Ventilació creuada és quan les obertures d'una sala es disposen en parets oposades (exemple:")
    print("porta oberta i finestres oposades obertes).En cas que tot estigui obert(portas obertes i finesres")    
    print("oposades i no oposades obertes),marcar la castilla de ventilació creuada. En cas que estiguui tot")
    print("tancat o només porta o finestres obertes, marca la casella de no ventilació creuada****")
    # options to choose
    print("Tria una de les opcions de ventilació creuada:")
    print("1: Si ventilació creuada")
    print("2: No ventilació creuada")
    num=int(input(""))
    # the validation of the options 
    while num < 1 or num> 2 :
        num=int(input("Elegir la opcion correcta  1 o 2 :"))
  
    print("\n")
    # printing the part 1 of the first page 
    print("Curso :",curso,"     ","Class :",clas,"     ","No. alumnes :",alum,"     ","No of Professors/es :",prof) 
    print("DIA :",dia,"              ","Hora de Clase :",dur)
    print("\n")
    
    # the table1
    for i in header :
        print(i, end=' \t\t|  ')
    print("")
    for i in range(7):
        print(dia ,' \t|   ' , hora[i] ,'\t\t|   ' ,co2llist[i] , ' \t\t|    ',templlist[i], '\t\t|   ' , humetatllist[i] , '\t\t|   ',nom_p , '\t\t|   ',assig, '\t\t| ')
    print("")        
    # the second table
    for i in header1 :
        print(i, end='\t| ')
    print("")
    print("\n","Pota Principal","\t",'oberta --> ',principal_obr,'min',"\n","Pota Principal","\t",'tencada --> ',principal_ten,'min',"\n","Pota Segungaria","\t",'oberta --> ',segun_obr,'min',"\n","Pota segundaria","\t",'tencada --> ',segun_ten,'min',"\n","finestres internes","\t",'oberta --> ',fin_in_obr,'min',"\n","finestres internes","\t",'tencada --> ',fin_in_ten,'min',"\n","finestres externes","\t",'oberta --> ',fin_ex_obr,'min',"\n","finestres externes","\t",'tencada --> ',fin_ex_ten,'min')
    print("")
    
    #printing one of the either option for the cross ventilation 
    if num == 1: 
        print("\n****Si ventilació creuada*****")
        
    elif num==2 : 
        print("\n****No ventilació creuada*****")



if __name__ == "__main__" :
    main()

