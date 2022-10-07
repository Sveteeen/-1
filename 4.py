Kolvo_let = int(input("Введите кол-во лет" ))
Kolvo_exponat = int(input( "Введите кол-во экспонатов" ))
T_for_1_expon = 5
T_for_1day = 8*60
expon_vden = T_for_1day / T_for_1_expon
dney = Kolvo_let * 365
Otvet1 = dney * expon_vden
Otvet2 = Kolvo_exponat / expon_vden
print( "За", Kolvo_let, " лет человек просмотрит", Otvet1, "экспонатов" )
print ( Kolvo_exponat, "экспонатов будет просмотрено за", Otvet2, "дней" )
                    
                
