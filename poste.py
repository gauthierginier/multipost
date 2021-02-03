import sys
import mysql.connector
from mysql.connector import Error
import argparse
import logging 

def connexionbdd(host, db, us, pw):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=db,
            user=us,
            password=pw)
        cursor = connection.cursor()
        print("connexion reussie")
        ajout_client(connection, cursor, 0, "kellian", "kellian@wtf.hard", "12 rue des platanes", "34000", "MTP", "0690123456")
        montrer_client(cursor, "kellian")
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connecté")
    except Exception as e:
        print(e)
        

# #Parser utilisateur : 
# parsed = argparse.ArgumentParser
# parsed.add_argument("-v", "--creerfacture", help="Créer facture")
# parsed.add_argument("-f", "--facture", help="Générer un numéro de facture unique")    
# parsed.add_argument("-d","--date_client",help="Générer une date d'émission client" )
# parsed.add_argument("-c","calcul",help="Calculer un prix à partir de chaque ligne" )
# parsed.add_argument("-s","--somme",help="effectuer la somme de toutes les valeurs de la table")
# parsed.add_argument("-r", "--rechercher" , help="rechercher une facture par son numéro")
# parsed.add_argument("-rechercher_date",help="Rechercher une facture par numéro et par date")
# parsed.add_argument("rechercher_fature_date", help="rechercher toutes les factures émises entre deux dates")
# parsed.add_argument("-ajout_client",help="ajouter un client manuellement 'entrez infos clavier'")
# parsed.add_argument("-m",help="modifier les informations d'un client")
# parsed.add_argument("-client_info",help="rechercher un client en fournissant son nom/email")
# parsed.add_argument("-s" , help="Supprimer des enregistrements")
# args = parser.parse_args()


# Def "montant total" par défaut calculé à partir des prix de chaque ligne: 
# def montant_total_lignes():
#   SELECT SUM (montant_total_facture)
#   FROM factures

# #effectuer la somme de toutes les valeurs de la table :
# #montant total (par défaut : calculé à partir des prix de chaque ligne)
# def somme_toutes_valeurs_table():
#   SELECT SUM(prix_unite  VALUE2) FROM factures
#   SUM(VALUE1 + VALUE2)



# #Def Générer une date d'émission client
# def date_emission_client():
#   cursor.execute (SELECT type_client, raison_sociale, email, adresse, tel
#   FROM facture)
#   rows = cursor.fetchall()
#   for row in rows:
#     print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))


# #Recherche facture par numéro et par date dans la bd
# def facture_numero_date ():
# #date
#   SELECT *, DATE_FORMAT(date_inscription, "%d/%m/%Y")
#   FROM facture AND ;


# # rechercher toutes les factures émises entre deux dates
# def facture_entre_deux_dates():
#   SELECT * FROM `table1`
#   INTERSECT
#   SELECT * FROM `table2`









# OK Ajouter une facture 
#  cursor.execute('INSERT INTO factures (type_client, raison_sociale, email, adresse, tel) VALUES (?,?,?,?,?,?,?,?)', (addf[0],addf[1],addf[2],addf[3], addf[4], addf[5],addf[6],addf[7]))


# #OK Supprimer des enregistrements dans la base de données
# def supprimer_enregistrement_bd(cursor):
#   cursor.execute("""DELETE FROM 'factures' """") 


# OK Ajouter un client manuellement
def ajout_client(connection, cursor, pro, nom, email, adresse, cp, ville, tel):
    cursor.execute('INSERT INTO client (entreprise, nom, email, adresse, codepostal, ville, tel) VALUES (%s,%s,%s,%s,%s,%s,%s);', (pro, nom, email, adresse, cp, ville, tel))
    connection.commit()
    print(cursor.rowcount, "record inserted.")
# OK rechercher un client en fournissant son nom et/ou son email
def montrer_client(cursor, nom):
    cursor.execute("""SELECT * FROM client WHERE nom LIKE %s """, (nom+'%',))
    response = cursor.fetchall()
    for row in response:
        print(row)

#OK rechercher une facture par numéro
# def facture_numero ():
#   cursor.execute("""SELECT  FROM factures WHERE '?' """, (rechf))


# #OK modifier les infos d'un client
# def modification_client():
#   cursor.execute("""UDPDATE client SET '?' = '?' WHERE '?' """, (modc[0], modc[1], modc[3]))





# #Gestion des erreurs : 
# # Veuillez saisir un argument 


if __name__ == "__main__":
    sys.exit(connexionbdd("192.168.1.3", "multipost", "machine", "aZeRtY123!" ))