'''
import os
import json
import pandas as pd


folder_path = os.getcwd() 


output_excel = "mahalle_listesi.xlsx"


data_list = []

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        

        il, ilce = os.path.splitext(filename)[0].split("-")
        

        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            
 
            for entry in json_data:
                mahalle, semt, posta_kodu = map(str.strip, entry.split("/"))
                data_list.append({
                    "İl": il.strip(),
                    "İlçe": ilce.strip(),
                    "Semt": semt.strip(),
                    "Mahalle": mahalle.strip(),
                    "Posta Kodu": posta_kodu.strip()
                })

df = pd.DataFrame(data_list)

df.to_excel(output_excel, index=False, encoding="utf-8", engine="openpyxl")

print(f"Veriler başarıyla {output_excel} dosyasına kaydedildi!")

'''
import os
import json
import pandas as pd


folder_path = os.getcwd()  


output_excel = "mahalle_listesi.xlsx"


data_list = []


for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        

        il, ilce = os.path.splitext(filename)[0].split("-")
        

        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            
 
            for entry in json_data:
                try:

                    mahalle, semt, posta_kodu = map(str.strip, entry.split("/"))
                    data_list.append({
                        "İl": il.strip(),
                        "İlçe": ilce.strip(),
                        "Semt": semt.strip(),
                        "Mahalle": mahalle.strip(),
                        "Posta Kodu": posta_kodu.strip()
                    })
                except ValueError:
                    print(f"Format hatası bulunan satır atlandı: {entry}")

df = pd.DataFrame(data_list)

df.to_excel(output_excel, index=False, engine="openpyxl")

print(f"Veriler başariyla {output_excel} dosyasina kaydedildi!")
