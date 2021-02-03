import sys
import mysql.connector
from mysql.connector import Error
import argparse
import logging
from getpass import getpass

#Parser utilisateur : 
parsed = argparse.ArgumentParser()
parsed.add_argument("-con", "--connexionfile",
                    help="Se connecter à l'aide d'un fichier",action="store_true", required=False )
parsed.add_argument("-a", "--ajout_client", help="increase output verbosity",
                    action="store_true", required=False)
parsed.add_argument("-m", "--modif_client", nargs=1, help="increase output verbosity", required=False)
parsed.add_argument("-c","--client_info",
                    nargs=1, help="rechercher un client en fournissant son nom/email", required=False)
parsed.add_argument("-f","--facture_info",
                    nargs=1, help="rechercher une facture en fournissant son numéro", required=False)
args = parsed.parse_args()


def connexionbdd():
    if args.connexionfile:
        with open("./loginfile.txt") as connexiondata:
            response = connexiondata.readlines()
            host = response[0].strip()
            db = response[1].strip()
            us = response[2].strip()
            pw = response[3].strip()
    else:
        host = input("Entrez l'adresse ip de votre serveur :\n")
        db = input("Entrez le nom de votre bdd :\n")
        us = input("Entrez votre identifiant :\n")
        pw = getpass(prompt='Entrez votre mot de passe : ')
    
    try:
        connection = mysql.connector.connect(
            host=host,
            database=db,
            user=us,
            password=pw)
        cursor = connection.cursor()
        print("connexion reussie")
        if args.ajout_client:
            ajout_client(connection, cursor)
        if args.modif_client:
            modif_client(connection, cursor, args.modif_client[0])
        if args.client_info:
            montrer_client(cursor, args.client_info[0])
        if args.facture_info:
            montrer_client(cursor, args.facture_info[0])
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connecté")
    except Exception as e:
        print(e)
        
def ajout_client(connection, cursor):
    print("MERCI DE RENSEIGNER LES INFOS DU NOUVEAU CLIENT :")
    pro = int(input("""ENTREZ 1 POUR UNE ENTREPRISE,\nOU 0 POUR UN PARTICULIER\n"""))
    nom = input("ENTREZ LE NOM DU CLIENT :\n")
    email = input("ENTREZ L'EMAIL DU CLIENT :\n")
    adresse = input("ENTREZ L'ADRESSE DU CLIENT :\n")
    cp = input("ENTREZ LE CODE POSTAL DU CLIENT :\n")
    ville = input("ENTREZ LE VILLE DU CLIENT :\n")
    tel = input("ENTREZ LE TEL DU CLIENT :\n")
    cursor.execute('INSERT INTO client (entreprise, nom, email, adresse, codepostal, ville, tel) VALUES (%s,%s,%s,%s,%s,%s,%s);', (pro, nom, email, adresse, cp, ville, tel))
    connection.commit()
    print(cursor.rowcount, "ligne(s) ajoutée(s).")
# OK rechercher un client en fournissant son nom et/ou son email
def montrer_client(cursor, nom):
    cursor.execute("""SELECT * FROM client WHERE nom LIKE %s OR email LIKE %s""", (nom+'%',nom+'%'))
    response = cursor.fetchall()
    for row in response:
        print(row)
def modif_client(connection, cursor, client):
    print("MERCI DE RENSEIGNER LES NOUVELLES INFOS DU CLIENT :")
    pro = int(input("""ENTREZ 1 POUR UNE ENTREPRISE,\nOU 0 POUR UN PARTICULIER\n"""))
    nom = input("ENTREZ LE NOM DU CLIENT :\n")
    email = input("ENTREZ L'EMAIL DU CLIENT :\n")
    adresse = input("ENTREZ L'ADRESSE DU CLIENT :\n")
    cp = input("ENTREZ LE CODE POSTAL DU CLIENT :\n")
    ville = input("ENTREZ LE VILLE DU CLIENT :\n")
    tel = input("ENTREZ LE TEL DU CLIENT :\n")
    cursor.execute(
        """UPDATE client SET
        entreprise = %s,
        nom = %s,
        email = %s,
        adresse = %s,
        codepostal = %s,
        ville = %s,
        tel  = %s
        WHERE id = %s ;""", (pro, nom, email, adresse, cp, ville, tel, client))
    connection.commit()
    print(cursor.rowcount, "ligne(s) modifiée(s).")
def montrer_facture(cursor, id):
    cursor.execute("""SELECT * FROM client WHERE id LIKE %s""", (id,))
    response = cursor.fetchall()
    for row in response:
        print(row)

if __name__ == "__main__":
    sys.exit(connexionbdd())