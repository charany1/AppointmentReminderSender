from db.FetchFromMySQL import *
from messaging.Sms import *
from datetime import  datetime,timedelta

def main():
    patient_for_sending_sms = get_patients_for_seding_sms()
    if patient_for_sending_sms is not None:
        for patient_record in patient_for_sending_sms:
            id,mobile,name,last_visit = patient_record
            mobile = "+91"+mobile
            message_body = "Hi {} ,\n Your next appointment is due on {}".format(name,last_visit+timedelta(days=30))
            send_message(message_body)



if __name__=="__main__":
    main()