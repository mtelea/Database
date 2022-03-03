from componente.BuildConnection import Connection

conexiune = Connection('localhost', 'root', 'Trestianr1', 'cosmeticswarehouse')
cursor = conexiune.getCursor()

def selectAllFromOrderBy(table, orderBy, asc):
    """
    :param table: Tabela
    :param orderBy: Coloana dupa care ordonezi
    :param asc : Ascendent(True) sau Descendent(False)
    :return: Rezultatele queryului sub forma de array de rows
    """
    if asc == True:
        sql = f"SELECT * FROM {table[0]} ORDER BY {orderBy}"
    else:
        sql = f"SELECT * FROM {table[0]} ORDER BY {orderBy} Desc"
    print(sql)
    cursor.execute(sql)
    header = cursor.description
    results = cursor.fetchall()
    return header, results

def commitSQL(cursor):
    """
    :param cursor: Cursorul MYSQL
    :return: void - doar executa comanda commit in BD
    """
    cursor.execute("commit")

def rollbackSQL(cursor):
    """
    :param cursor: Cursorul MYSQL
    :return: void - doar executa comanda commit in BD
    """
    cursor.execute("rollback")

def getAllTables():
    """
    :return: lista cu tabelele
    """
    cursor.execute("show tables")
    return cursor.fetchall()

def getAllColumnsFromTable(table):
    cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{table}'")
    return cursor.fetchall()

def solveCerintaC():
    cursor.execute("""select prod_ID,p.nume,pret,data_plasare,r.nume 
                    from produs_cosmetic p join detalii_comanda using (prod_ID)
                    join comanda using (comanda_ID) join retailer r using (retailer_ID)
                    where (retailer_ID = 2 )
                    and (status_comanda like "livrata")""")
    header = cursor.description
    results =cursor.fetchall()
    return header, results

def solveCerintaD():
    cursor.execute("""select ingr_ID, denumire,concentratie,count(prod_ID) as 'Numar Produse'
                    from produs_cosmetic left join produs_ingredient using (prod_ID) join ingredient_activ using (ingr_ID)
                    group by (ingr_ID)
                    having concentratie >1;""")
    header = cursor.description
    results = cursor.fetchall()
    return header, results
