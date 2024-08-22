import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import os
import unicodedata


prov = input("de que provincia vamos a extraer la informacion? ")
city = input(f"de que ciudad de {prov} vamos a extraer la informacion? ")

filename = f'{prov}_{city}.xlsx'

if os.path.exists(filename):
    # Si el archivo existe, lo carga
    book = openpyxl.load_workbook(filename)
else:
    # Si el archivo no existe, lo crea
    book = openpyxl.Workbook()
    




pcity = city.replace(' ','-')
ppcity = pcity.replace('í','i')
pppcity = ppcity.replace('ó','o')
new_city = pppcity.lower()



sheet = book.active
sheet['A1'] = 'precio,nombre,metros cuadrados,ambientes,dormitorios,banios,cochera'
        


for pi in range(1,50): 
    
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()   
        driver.get(f"https://www.zonaprop.com.ar/casas-venta-pagina-{pi}-q-{new_city}.html")
        time.sleep(3)
        if (pi > 1):
            pagC = str(driver.current_url)
            pagR = pagC.replace('https://www.zonaprop.com.ar/casas-venta-pagina-','')
            pag = pagR.replace(f'-q-{new_city}.html','')
            paginaActual = int(pag)
            if (paginaActual < pi):
                break
        listaTotal = []
    
        posicion = 0
        
        precios = driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "geYYII", " " ))]')

    
        for i in precios:
        
            Pprecio = i.text
        
            precio = Pprecio.replace('USD ','')
        
            precioR = precio.replace('.','')
    
        
            listaTotal.append(precioR)
        
            posicion+=1

    
        posicion = 0

    
        nombres = driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "postingAddress", " " ))]')

    
        for i in nombres:
        
            nombre = i.text
        
            def eliminar_diacriticos(texto):
                # Normaliza el texto a forma 'NFD' que separa los caracteres y sus diacríticos
                texto_normalizado = unicodedata.normalize('NFD', texto)
                # Filtra los caracteres que no son diacríticos
                texto_sin_diacriticos = ''.join(caracter for caracter in texto_normalizado if unicodedata.category(caracter) != 'Mn')
                # Normaliza de nuevo a la forma 'NFC' para reconstruir el string
                return texto_sin_diacriticos    
            
            nombree = eliminar_diacriticos(nombre)
            
            while ('º' in nombree):
        
                nombree = nombree.replace('º','')
            
            
            while (',' in nombree):
        
                nombree = nombree.replace(',','')
        
            while ('ñ' in nombree):
        
                nombree = nombree.replace('ñ','n')    
            
            
            while ('°' in nombree):
        
                nombree = nombree.replace('°','')
        
            try:


        
                listaTotal[posicion] += f',{nombree}'
        
                posicion+=1
        
            except:
        
                pass
    

    
        posicion = 0

    
        Mcuadrados = driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "cHDgeO", " " ))]//span[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]')

    
        for i in Mcuadrados:
    
        
            try:
        
                metros = i.text
        
                metrosr = metros.replace(' m² tot.','')
        
                listaTotal[posicion] += f',{metrosr}'
        
                posicion+=1
        
            except:
        
                pass
    
       
    
        posicion = 0
       
    
        todosLosAmbientes = driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "cHDgeO", " " ))]//span[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]')

    
        for i in todosLosAmbientes:
    
        
            try:
        
                ambientesR = i.text
        
                ambientes = ambientesR.replace(' amb.','')
        
                listaTotal[posicion] += f',{ambientes}'
        
                posicion+=1
        
            except:
        
                pass

    
        posicion = 0

    
        todosLosDormitorios = driver.find_elements(By.XPATH, '//span[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]')

    
        for i in todosLosDormitorios:
    
    
        
            try:
        
                dormitoriosR = i.text
        
                dormitorios = dormitoriosR.replace(' dorm.','')
        
                listaTotal[posicion] += f',{dormitorios}'
        
                posicion+=1
        
            except:
        
                pass

    
        posicion = 0

    
        todosLosbaños = driver.find_elements(By.XPATH, '//span[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]')

    
        for i in todosLosbaños:
    
    
        
            try:
        
                bañosR = i.text
        
                baños = bañosR.replace(' baños','')
        
                bañosrr = baños.replace(' baño','')
        
                listaTotal[posicion] += f',{bañosrr}'
        
                posicion+=1
        
            except:
        
                pass

    
        posicion = 0


    
        coch = 1
    
        while coch < 30:
    
        
            try:
        
                lascocheras = driver.find_element(By.XPATH, f'//*[contains(concat( " ", @class, " " ), concat( " ", "fvuHxG", " " )) and (((count(preceding-sibling::*) + 1) = {coch}) and parent::*)]//span[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]')
        
                cocherasR = lascocheras.text
        
                cocheras = cocherasR.replace(' coch.','')
        
            except Exception:
        
                cocheras = "0"
    
        
            print(cocheras)
    
        
            try:
        
                listaTotal[posicion] += f',{cocheras}'
        
            except:
        
                pass
    
        
            posicion += 1
        
            coch += 1
    
        for i in range(len(listaTotal)):
        
            init = listaTotal[i]
        
            a = init.replace(' m² tot.','')
        
            aa = a.replace(' amb.','')
        
            aaa = aa.replace(' dorm.','')
        
            aaaa = aaa.replace(' baños','')
        
            aaaaa = aaaa.replace(' baño','')
        
            aaaaaa = aaaaa.replace(' coch.','')
        
            listaTotal[i] = aaaaaa
    
        print(' \n')
    
        print(listaTotal)

        #  venta-pagina-1-q
        
        
        n = 2+(30*(pi-1))
    
        for i in range(len(listaTotal)):
            sheet[f'A{n}'] = listaTotal[i]
            n += 1
        
        
        
        
            
        # pyautogui.write(['-', 'p', 'a', 'g', 'i', 'n', 'a', '-', f'{i}'])
        # time.sleep(2)
        # pyautogui.press('enter')
        
        driver.close()
    except:
        pass
    
        
driver.quit()
time.sleep(1)
book.save(filename)       


