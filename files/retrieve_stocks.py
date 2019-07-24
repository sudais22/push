import psycopg2 as p

def getStockData():
    connection = 0
    try:
        connection = p.connect(user="postgres",
                               password="postgres",
                               host="172.17.0.2",
                               port="5432",
                               database="postgres")
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("Connection established to: ", record,"\n")
    except (Exception, p.Error) as error:
        print("Error while connecting to PostgreSQL: ", error, "\n")
    finally:
        if(connection):
            #retrieveStocks = "SELECT row_to_json(row(day, closing_price, volume)) FROM stocktrade order by day ASC"
            retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade order by day ASC) d ) as info) t "
            cursor.execute(retrieveStocks)
            result = cursor.fetchall()
            return result
        else:
            return 0
        cursor.close()
        connection.close()
        print("Disconnected from postgreSQL")



