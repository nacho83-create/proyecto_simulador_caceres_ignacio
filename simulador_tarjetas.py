print("================================================================")
print("BIENVENIDOS AL SIMULADOR DE INTERESES DE TARJETAS DE CREDITO")
print("================================================================")
def main():
    print("************************************************************")
    print("MENU INTERACTIVO")
    print("************************************************************")
    print("")
    print("""[1] - Tarjeta visa, mastercard, american express bancaria 
    hasta 6 cuotas""")
    print("")
    print("""[2] - Tarjeta visa, mastercard, american express no bancaria
    hasta 6 cuotas""")
    print("")
    print("""[3] - Tarjeta naranja en planes hasta 6 cuotas""")
    print("")
    print("[4] - Tarjeta naranja en plan z")
    print("")
    print("""[5] - Tarjeta patagonia 365 hasta 6 cuotas""")
    print("")
    print("[6] - Salir del sistema")
    print("")
    print("************************************************************")
    print("============================================================")
    opcion= int(input("Por favor ingrese la opcion deseada:"))
    print("============================================================")
    print("************************************************************")
    if opcion==1:
        print("Por favor ingrese a continuacion el monto total de la compra realizada:")
        monto= float(input('monto total:'))
        print("============================================================")
        print("Por favor a continuacion ingrese la cantidad de cuotas:")
        cuotas= int(input("cuotas:"))
        if cuotas==1:
            monto=monto*1.05
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE: $",monto)
            print("************************************************************")
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()
            else: 
                def error():
                    print("************************************************************")
                    menu=int(input("opcion incorrecta presione 0 para volver al menu principal:"))
                    print("************************************************************")
                    if menu==0:
                         main()
                    else:
                        error()    
                error()
                

        elif cuotas==2:
            monto2=monto*1.1307
            cuota2=monto2/2
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto2)
            print("CON DOS CUOTAS DE :$", cuota2,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************") 
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()
        elif cuotas==3:
            monto3=monto*1.1786
            cuota3=monto3/3
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto3)
            print("CON TRES CUOTAS DE :$", cuota3,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************") 
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()  
        elif cuotas==4:
            monto4=monto*1.2279
            cuota4=monto4/4
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto4)
            print("CON CUATRO CUOTAS DE :$", cuota4,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()  
        elif cuotas==5:
            monto5=monto*1.2784
            cuota5=monto5/5
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto5)
            print("CON CINCO CUOTAS DE :$", cuota5,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()
        elif cuotas==6:
            monto6=monto*1.3302
            cuota6=monto6/6
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto6)
            print("CON SEIS CUOTAS DE :$", cuota6,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************") 
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()   
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("La opcion ingresada no es valida, el comercio solo vende hasta 6 cuotas") 
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main() 
    elif opcion==2:
        print("=================================================================")
        print("Por favor ingrese a continuacion el monto total de la compra realizada:")
        monto= float(input('monto total:'))
        print("============================================================")
        print("Por favor a continuacion ingrese la cantidad de cuotas:")
        cuotas= int(input("cuotas:"))
        if cuotas==1:
            monto=monto*1.05
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE: $",monto)
            print("************************************************************")
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()

            
        elif cuotas==2:
            monto2=monto*1.1466
            cuota2=monto2/2
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto2)
            print("CON DOS CUOTAS DE :$", cuota2,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()
        elif cuotas==3:
            monto3=monto*1.2007
            cuota3=monto3/3
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto3)
            print("CON TRES CUOTAS DE :$", cuota3,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()  
        elif cuotas==4:
            monto4=monto*1.2564
            cuota4=monto4/4
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto4)
            print("CON CUATRO CUOTAS DE :$", cuota4,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()  
        elif cuotas==5:
            monto5=monto*1.3137
            cuota5=monto5/5
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto5)
            print("CON CINCO CUOTAS DE :$", cuota5,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()
        elif cuotas==6:
            monto6=monto*1.3726
            cuota6=monto6/6
            print("************************************************************")
            print("LA COMPRA TOTAL SERA DE:$",monto6)
            print("CON SEIS CUOTAS DE :$", cuota6,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()   
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("La opcion ingresada no es valida, el comercio solo vende hasta 6 cuotas") 
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main() 
    elif opcion==3:
        print("============================================================")
        print("Por favor ingrese a continuacion el monto total de la compra realizada:")
        monto= float(input('monto total:'))
        print("============================================================")
        print("Por favor a continuacion ingrese la cantidad de cuotas:")
        cuotas= int(input("cuotas:"))
        if cuotas==1:
            print("************************************************************")
            monto=monto*1.05
            print("LA COMPRA TOTAL EN NARANJA SERA DE: $",monto)
            print("************************************************************")
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()

            
        elif cuotas==2:
            monto2=monto*1.1466
            cuota2=monto2/2
            print("************************************************************")
            print("LA COMPRA TOTAL EN NARANJA SERA DE:$",monto2)
            print("CON DOS CUOTAS DE :$", cuota2,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()
        elif cuotas==3:
            monto3=monto*1.2007
            cuota3=monto3/3
            print("************************************************************")
            print("LA COMPRA TOTAL EN NARANJA SERA DE:$",monto3)
            print("CON TRES CUOTAS DE :$", cuota3,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()  
        elif cuotas==4:
            monto4=monto*1.2564
            cuota4=monto4/4
            print("************************************************************")
            print("LA COMPRA TOTAL EN NARANJA SERA DE:$",monto4)
            print("CON CUATRO CUOTAS DE :$", cuota4,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()  
        elif cuotas==5:
            monto5=monto*1.3137
            cuota5=monto5/5
            print("************************************************************")
            print("LA COMPRA TOTAL EN NARANJA SERA DE:$",monto5)
            print("CON CINCO CUOTAS DE :$", cuota5,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()
        elif cuotas==6:
            monto6=monto*1.3726
            cuota6=monto6/6
            print("************************************************************")
            print("LA COMPRA TOTAL EN NARANJA  SERA DE:$",monto6)
            print("CON SEIS CUOTAS DE :$", cuota6,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()   
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("La opcion ingresada no es valida, el comercio solo vende hasta 6 cuotas") 
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main() 
    elif opcion==4:
        print("============================================================")
        print("Por favor ingrese a continuacion el monto total de la compra realizada en plan z:")
        monto= float(input('monto total:'))
        montoz=monto*1.15
        print("************************************************************")
        print("LA COMPRA TOTAL EN PLAN Z SERA DE: $",montoz)
        print("************************************************************")
        print("============================================================")
        menu=int(input("presione 0 para volver al menu principal:"))
        if menu==0:
             main()


    elif opcion==5:
        print("============================================================")
        print("Por favor ingrese a continuacion el monto total de la compra realizada con patagonia 365:")
        monto= float(input('monto total:'))
        print("============================================================")
        print("Por favor a continuacion ingrese la cantidad de cuotas:")
        cuotas= int(input("cuotas:"))
        if cuotas==1:
            print("************************************************************")
            monto=monto*1.05
            print("LA COMPRA TOTAL EN PATAGONIA 365 SERA DE: $",monto)
            print("************************************************************")
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()

            
        elif cuotas==2:
            monto2=monto*1.15
            cuota2=monto2/2
            print("************************************************************")
            print("LA COMPRA TOTAL EN PATAGONIA 365 SERA DE:$",monto2)
            print("CON DOS CUOTAS DE :$", cuota2,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()
        elif cuotas==3:
            monto3=monto*1.15
            cuota3=monto3/3
            print("************************************************************")
            print("LA COMPRA TOTAL EN PATAGONIA 365 SERA DE:$",monto3)
            print("CON TRES CUOTAS DE :$", cuota3,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()  
        elif cuotas==4:
            monto4=monto*1.15
            cuota4=monto4/4
            print("************************************************************")
            print("LA COMPRA TOTAL EN PATAGONIA 365 SERA DE:$",monto4)
            print("CON CUATRO CUOTAS DE :$", cuota4,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================") 
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()  
        elif cuotas==5:
            monto5=monto*1.15
            cuota5=monto5/5
            print("************************************************************")
            print("LA COMPRA TOTAL EN PATAGONIA 365 SERA DE:$",monto5)
            print("CON CINCO CUOTAS DE :$", cuota5,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================")  
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()
        elif cuotas==6:
            monto6=monto*1.15
            cuota6=monto6/6
            print("************************************************************")
            print("LA COMPRA TOTAL EN PATAGONIA 365 SERA DE:$",monto6)
            print("CON SEIS CUOTAS DE :$", cuota6,"APROXIMADAMENTE")
            print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS") 
            print("************************************************************")
            print("============================================================")  
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main()   
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("La opcion ingresada no es valida, el comercio solo vende hasta 6 cuotas") 
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("============================================================")
            menu=int(input("presione 0 para volver al menu principal:"))
            if menu==0:
                main() 
    elif opcion==6:
        print("============================================================")
        print("MUCHAS GRACIAS POR USAR EL SIMULADOR DE CUOTAS")
        print("============================================================")
        
    else:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("La opcion ingresada no es valida, el comercio solo vende hasta 6 cuotas") 
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("============================================================")
        menu=int(input("presione 0 para volver al menu principal:"))
        if menu==0:
             main() 
main()