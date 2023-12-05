# # TP Data Analyst

# Vous êtes consultant Data analyst vous avez été missionnée chez 2 clients : 

# ## Client 1 : Concession automobile

# En vous basant sur les données fournies, vous devez aider Monsieur Arnaud qui a comme projet d'installer une concession automobile dans la ville de Frankfort. Monsieur Arnaud a fait une etude de marché sur la population de Frankfort et elle definit cette population de relativement aisée. 

# Les données : https://mohamed-demo-neosoft.s3.us-east-2.amazonaws.com/cleaned_autos.csv

# Il vous a mis à disposition un certain volume de donnée, il voudrait que vous l'aidiez, dans un premier temps, à extraire un certain nombre d'informations des données : 

#  - Nombre total de véhicules en vente selon le type de véhicule.
#  - Répartition des véhicules en fonction de l'année d'immatriculation
#  - Nombre de véhicules par marque
#  - Prix moyen des véhicules par type de véhicule et type de boîte de vitesses
#  - Prix moyen des véhicules selon le type de carburant et le type de boîte de vitesses

# Chacune de ces informations doivent être modélisé sous la forme d'un graphique adapté. Il faudra utiliser le plus possible des graphiques différents et variés.

# Dans la ville de Frankfort, il existe dejà de nombreuses concessions dans cette ville. Mais il voudrait une concession exclusivement pour la partie aisée de la population. 

# Il voudrait savoir quelles sont les 2 marques principales qu'il pourrait avoir dans sa concession et les 2 catégories de véhicule (en lien avec les 2 marques) qui colleraient le mieux à la population aisée, toujours dans sa concession. Il faudra donc trouver les Prix moyens des véhicules par type de véhicule et marque.

# Avec une dernière représentation graphique sous forme de heatmap, il faudra le convaincre de la solution que vous réussi à extraire de votre analyse.


import mysql.connector, csv
import pandas as pd
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

file_path="./cleaned_autos.csv"
df_auto=pd.read_csv(file_path)

##/!\/!\ EXECUTER EXERCICE PAR EXERCICE /!\/!\

#1)
# df_auto_type=df_auto.groupby('vehicleType').size().rename('count_type').reset_index()
# print(df_auto_type)

# x=df_auto_type["vehicleType"]
# y=df_auto_type['count_type']

# plt.style.use('Solarize_Light2') #-> style.use permet de prédéfinir des couleurs partout
# plt.pie(y,labels=x,autopct='%1.1f%%') #,hatch=['**O', 'oO'] pour style dég
# plt.title('Nbr Exemplaire Par Type Véhicule')
# plt.savefig("Nbr_Exemplaire_Par_Type_Véhicule_PIE.png")

# plt.show()
# plt.style.use('Solarize_Light2') #-> style.use permet de prédéfinir des couleurs partout
# plt.bar_label(container=plt.bar(x,y, zorder=2))#-> histogramme
# # plt.plot(x,y,label='zboub',linestyle='dotted') #->courbe
# #linestyle change la forme de la ligne (ici enpointillé)
# plt.xlabel("type Véhicule") #->titre des abscisses
# plt.ylabel("Nombre Exemplaire") #-> titre des ordonnées
# # plt.xlim(left=0,right=10) #où commencent, terminent abscisses
# # plt.ylim(bottom=0,top=10) #où commencent, terminent ordonnées
# plt.title('Nbr Exemplaire Par Type Véhicule') #-> titre global
# plt.legend() #affiche légend mais necessite label (ici dans plt.plot et plt.bar)
# plt.savefig("Nbr_Exemplaire_Par_Type_Véhicule.png")

# plt.show()

# #2)
# df_auto_year=df_auto.groupby('yearOfRegistration').size().rename('count_year_regis').reset_index()

# x=df_auto_year["yearOfRegistration"]
# y=df_auto_year['count_year_regis']


# plt.style.use('Solarize_Light2') #-> style.use permet de prédéfinir des couleurs partout

# plt.plot(x,y) #->courbe

# plt.xlabel("Année d'Immatriculation") #->titre des abscisses
# plt.ylabel("Nombre Véhicule") #-> titre des ordonnées

# plt.title('Nbr Véhicule Par Année Immatriculation') #-> titre global
# plt.legend() #affiche légend mais necessite label (ici dans plt.plot et plt.bar)
# plt.savefig("Nbr_Exemplaire_Par_Year._Registration.png")

# plt.show()


# #3)
# df_auto_brand=df_auto.groupby('brand').size().rename("count_brand").reset_index()

# x=df_auto_brand["brand"]
# y=df_auto_brand['count_brand']


# plt.style.use('Solarize_Light2') #-> style.use permet de prédéfinir des couleurs partout
# plt.bar_label(container=plt.barh(x,y, zorder=2))#-> histogramme


# plt.xlabel("Nombre Véhicule") #->titre des abscisses
# plt.ylabel("Marque Véhicule") #-> titre des ordonnées

# plt.title('Nbr Véhicule Par Marque') #-> titre global
# plt.legend() #affiche légend mais necessite label (ici dans plt.plot et plt.bar)
# plt.savefig("Nbr_Exemplaire_Par_Marque.png")

# plt.show()

# #4)
# df_vente_type_gearbox=df_auto.groupby(["vehicleType","gearbox"])["price"].mean().rename('Moy_vente_type_gearbox').reset_index()
# print(df_vente_type_gearbox)

# df_vente_type_manu=df_vente_type_gearbox[df_vente_type_gearbox['gearbox']=='manuell']
# df_vente_type_unspe=df_vente_type_gearbox[df_vente_type_gearbox['gearbox']=='Unspecified']
# df_vente_type_auto=df_vente_type_gearbox[df_vente_type_gearbox['gearbox']=='automatik']

# print(df_vente_type_manu)
# # print(df_vente_type_unspe)
# # print(df_vente_type_auto)

# x1=df_vente_type_manu.index
# y1=df_vente_type_manu["Moy_vente_type_gearbox"]
# x2=df_vente_type_unspe.index
# y2=df_vente_type_unspe["Moy_vente_type_gearbox"]
# x3=df_vente_type_auto.index
# y3=df_vente_type_auto["Moy_vente_type_gearbox"]


# plt.style.use('Solarize_Light2') #-> style.use permet de prédéfinir des couleurs partout
# plt.bar_label(container=plt.bar(x1-0.3,y1, label="manuelle" ))
# plt.bar_label(container=plt.bar(x2+0.3,y2, label="non spécifié" ))
# plt.bar_label(container=plt.bar(x3,y3, label="automatique" ))

# plt.xlabel("Type Véhicule") #->titre des abscisses
# plt.ylabel("Moyenne de Vente") #-> titre des ordonnées

# plt.xticks(x3,df_vente_type_auto['vehicleType']) #1er arg => espacement des sticks, 2eme => ce qui est affiché

# plt.title('Moyenne Vente Par Type Véhicule et Gearbox') #-> titre global
# plt.legend() #affiche légend mais necessite label (ici dans plt.plot et plt.bar)
# plt.savefig("Moy_Vente_Type_Gearbox.png")

# plt.show()
# print(plt.style.available)


# #5)
# df_vente_fuel_gearbox=df_auto.groupby(["fuelType","gearbox"])["price"].mean().rename('Moy_vente_fuel_gearbox').reset_index()
# print(df_vente_fuel_gearbox)


# df_vente_fuel_manu=df_vente_fuel_gearbox[df_vente_fuel_gearbox['gearbox']=='manuell']
# df_vente_fuel_unspe=df_vente_fuel_gearbox[df_vente_fuel_gearbox['gearbox']=='Unspecified']
# df_vente_fuel_auto=df_vente_fuel_gearbox[df_vente_fuel_gearbox['gearbox']=='automatik']

# print(df_vente_fuel_manu)
# print(df_vente_fuel_unspe)
# print(df_vente_fuel_auto)

# x1=df_vente_fuel_manu.index
# y1=df_vente_fuel_manu["Moy_vente_fuel_gearbox"]
# x2=df_vente_fuel_unspe.index
# y2=df_vente_fuel_unspe["Moy_vente_fuel_gearbox"]
# x3=df_vente_fuel_auto.index
# y3=df_vente_fuel_auto["Moy_vente_fuel_gearbox"]


# plt.style.use('dark_background') #-> style.use permet de prédéfinir des couleurs partout
# plt.bar_label(container=plt.bar(x1-0.3,y1, label="manuelle" ))
# plt.bar_label(container=plt.bar(x2+0.3,y2, label="non spécifié" ))
# plt.bar_label(container=plt.bar(x3,y3, label="automatique" ))

# plt.xlabel("Carburant") #->titre des abscisses
# plt.ylabel("Moyenne de Vente") #-> titre des ordonnées

# plt.xticks(x3,df_vente_fuel_auto['fuelType']) #1er arg => espacement des sticks, 2eme => ce qui est affiché

# plt.title('Moyenne Vente Par Carburant et Gearbox') #-> titre global
# plt.legend() #affiche légend mais necessite label (ici dans plt.plot et plt.bar)
# plt.savefig("Moy_Vente_Fuel_Gearbox.png")

# plt.show()
# print(plt.style.available)



#6) option 1
# df_vente_type_brand=df_auto.groupby(["vehicleType","brand"])["price"].mean().rename('Moy_vente_fuel_gearbox').reset_index()

# df_fin=df_vente_type_brand.pivot(index='vehicleType', columns='brand', values='Moy_vente_fuel_gearbox')
# df_fin=df_fin.fillna(float(0))
# df_fin=df_fin.astype('int32')


# print(df_fin)
# plt.imshow(df_fin)
# plt.tight_layout()

# x=list(df_vente_type_brand.groupby('vehicleType').size().index)
# y=list(df_vente_type_brand.groupby('brand').size().index)


# plt.xticks(range(len(y)),y)
# plt.yticks(range(len(x)),x)
# plt.show()

#option2
import seaborn as sns
df_vente_type_brand=df_auto.groupby(["vehicleType","brand"])["price"].mean().rename('Moy_vente_fuel_gearbox').reset_index()
df_fin=df_vente_type_brand.pivot(index='vehicleType', columns='brand', values='Moy_vente_fuel_gearbox')
df_fin=df_fin.fillna(float(0))
df_fin=df_fin.astype('int32')
sns.heatmap(df_fin, annot=True, fmt="d", linewidths=0.5, cmap='plasma')

x=list(df_vente_type_brand.groupby('vehicleType').size().index)
y=list(df_vente_type_brand.groupby('brand').size().index)

plt.xticks(range(len(y)),y)
plt.yticks(range(len(x)),x)
plt.show()

