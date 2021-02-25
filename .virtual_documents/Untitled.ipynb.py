import random
import pandas as pd
from datetime import datetime 
from pandas import ExcelWriter


df = pd.read_csv("Archive_Soldes_generated.csv",header=None,index_col=0)
df.columns=["Debtor","Date","Solde"]
print(df)
print(df.dtypes)
df['Date'] =  pd.to_datetime(df['Date'], format='get_ipython().run_line_magic("Y-%m-%d')", "")
print(df.dtypes)
df.sort_values(["Debtor"],ascending=True, inplace=True) 
all_id = pd.unique(df["Debtor"].sort_values())


df.groupby(['Date'])['Solde'].sum().sort_values(ascending=True)


df.groupby(['Debtor'])['Solde'].sum().sort_values(ascending=True)


#Extraire les soldes qui ont dépassé 5M par jour

res33 = {}
res5 = pd.DataFrame(columns = ["Debtor","Date","Solde","Succession"])
for i in all_id:
    recurr_totale = 0 # Compteur de cmb de période de succesion au total ?
    occ_succ = 0 # Compteur cmb de jours successifs ?
    dfIndividu = df.query('Debtor == {}'.format(i))
    dfIndividu.reset_index(drop=True, inplace=True)
    #print(dfIndividu)
    ancien = False
    for k in range(dfIndividu.shape[0]):
        if dfIndividu["Solde"].iloc[k] <= -5000000:
            occ_succ += 1
            dfResult = pd.DataFrame({"Debtor":[dfIndividu["Debtor"].iloc[k]],"Date":[dfIndividu["Date"].iloc[k]],"Solde":[dfIndividu["Solde"].iloc[k]],"Succession":[occ_succ]})
            res5 = pd.concat([res5,dfResult])
            nouveau = True
        else: #recurr_totale +=1 # cmb de fois et cmb de période dans son historique le cdf a succédé 5m
            occ_succ = 0 # jtrouve pas de succession, remise du compteur à 0
            nouveau = False

        if(ancien get_ipython().getoutput("= nouveau and ancien==False):")
            recurr_totale += 1
        ancien = nouveau
    res33[i] = recurr_totale
print("Done get_ipython().getoutput("")")


res5.reset_index(drop=True, inplace=True)
print(res5)
res5id = pd.unique(res5["Debtor"].sort_values())

for k in list(res33):
    if k not in res5id:
        res33.pop(k)
print()
print()
res33 = pd.DataFrame(res33.items(), columns=['Debtor', 'Récurrence'])
print(res33)


listRes = []
res3 = {}
res3j = pd.DataFrame(columns = ["Debtor","Date","Solde","Occurrences sucessives"])
for i in all_id:
        recurr_totale = 0 # Compteur de cmb de période de succesion au total ?
        occ_succ = 0 # Compteur cmb de jours successifs ?
        cpt=0
        dfIndividu = df.query('Debtor == {}'.format(i))
        dfIndividu.reset_index(drop=True, inplace=True)
        ancien = False
        
        for index,rows in dfIndividu.iterrows():
            if rows['Solde'] <= -3000000:
                cpt += 1
                occ_succ += 1
                listTemp = [rows['Debtor'],rows['Date'],rows['Solde'],occ_succ]
                listRes.append(listTemp)
                nouveau = True
            if (rows['Solde'] > -3000000 or index == dfIndividu.shape[0]-1 ): #recurr_totale +=1 # cmb de fois et cmb de période dans son historique le␣cdf a succédé 5m
                if cpt>=3:
                    res3j = pd.concat([res3j, pd.DataFrame(listRes,columns = ["Debtor","Date","Solde","Occurrences sucessives"])])
                    recurr_totale += 1
                cpt=0
                occ_succ = 0 # jtrouve pas de succession, remise du compteur à 0
                nouveau = False
                listRes=[]

        res3[i] = recurr_totale

print("Done get_ipython().getoutput("")")



res3j.reset_index(drop=True, inplace=True)
print(res3j)
res5id = pd.unique(res3j["Debtor"].sort_values())
for k in list(res3):
    if k not in res5id:
        res3.pop(k)
print()
print()
res3 = pd.DataFrame(res3.items(), columns=['Debtor', 'Récurrence'])
print(res3)


with ExcelWriter("Reporting Caisse.xlsx") as writer:
    start_row = 1
    res5.to_excel(writer, sheet_name=">5M", startrow=start_row, header = True)
    res33.to_excel(writer, sheet_name="Récurrences", startrow=start_row, header = True)
    res3j.to_excel(writer, sheet_name=">3M", startrow=start_row, header = True)
    res3.to_excel(writer, sheet_name="Récurrences 3J", startrow=start_row, header = True)
    writer.save()



