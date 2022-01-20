import mysql.connector  as mysqlpyth

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor

    bdd = mysqlpyth.connect(user='root', password='root', host='localhost', port="8081", database='brief_flask')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()

def lire_pages_dont():
    global cursor
    
    connexion()
    query = "SELECT * FROM pages_dons"
    cursor.execute(query)
    dons =[]

    for enregistrement in cursor :
        don = {}
        don['id_dons'] = enregistrement[0]
        don['nom'] = enregistrement[1]
        don['prenom'] = enregistrement[2]
        don['adresse'] = enregistrement[3]
        don['mail'] = enregistrement[4]
        don['somme'] = enregistrement[5]
        dons.append(don)

    deconnexion()
    return dons

def set_dons():
    global cursor

    connexion()
    query = "SELECT * FROM pages_dons"
    cursor.execute(query)
    dont = []
# query = "SELECT libelle FROM droits"+JOIN utilisateur ON droits.id_droits = utilisateur.droit WHERE utilisateurs.nom = %s AND utilisateurs.nom =%s"
    for enregistrement in cursor :
       donation = {}
       donation['id_dons'] = enregistrement[0]
       donation['nom'] = enregistrement[1]
       donation['prenom'] = enregistrement[2]
       donation['adresse'] = enregistrement[3]
       donation['mail'] = enregistrement[4]
       donation['somme'] = enregistrement[5]
       dont.append(donation)
    

    deconnexion()
    return dont
   
def somme():
    connexion()
    total=0
    query="SELECT * FROM pages_dons"
    cursor.execute(query)
    for enregistrement in cursor:
        total +=enregistrement[5]
    deconnexion()
    return (total) 
   
def set_datas(nom, prenom, adresse, mail, somme):
    global cursor
    global bdd

    connexion()
    
    print('verif',nom, prenom, adresse, mail, somme)
    #query = 'INSERT INTO pages_dons(nom, prenom, adresse, mail, somme)VALUES (?,?,?,?,?) """,(nom, premon, adresse, email, somme));'
    query = 'INSERT INTO pages_dons(nom, prenom, adresse, mail, somme) VALUES ("'+nom+'","'+prenom+'","'+adresse+'","'+mail+'","'+somme+'");'
    
    cursor.execute(query)
    bdd.commit()

    deconnexion()