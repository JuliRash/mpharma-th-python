from celery import shared_task
from django.core.mail import send_mail
from api.models import Diagnosis
import pandas as pd


@shared_task
def send_email(email):
    send_mail(
        'CSV import python django',
        'Congratulations your file has been imported successfully 🎊 🎉!.',
        'idowujulius92@gmail.com',
        [email],
        fail_silently=False,
    )

    return 'Message Sent to ' + email


@shared_task
def import_data_to_db(reader, email):
    j = pd.read_json(reader, dtype=True)
    for _, row in j.iterrows():
        if(row[0] != None and row[1] != None and row[2] != None and row[3] != None and row[4] != None and row[5] != None):
            created = Diagnosis.objects.create(
                category_code=row[0],
                category_title=row[5],
                diagnosis_code=row[1],
                full_code=row[2],
                abbreviated_description=row[3],
                full_description=row[4],
            )

    send_email.delay(email)
    return 'Data Imported Succcessfully'
