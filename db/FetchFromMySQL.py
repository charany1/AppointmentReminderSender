import pymysql.cursors


def create_and_get_connection(host="localhost",user="root",password="12345678",db="PatientData"):
    connection = pymysql.connect(host=host,user=user,password=password,db=db)
    return connection

def get_all_patients():
    connection = create_and_get_connection()
    get_all_patient_sql = "SELECT * FROM `appointement`";
    try:
        with connection.cursor() as cursor:
            cursor.execute(get_all_patient_sql)
            result = cursor.fetchone()
            print(result)

    finally:
        connection.close()


def get_patients_for_seding_sms():
    connection = create_and_get_connection()
    get_all_patient_sql = "select * from `appointement` where `last_visit` < curdate()-14";
    try:
        with connection.cursor() as cursor:
            cursor.execute(get_all_patient_sql)
            result = cursor.fetchall()
            return result

    finally:
        connection.close()


if __name__=="__main__":
    get_patients_for_seding_sms()
