from datetime import datetime
import smtplib, ssl
from email.message import EmailMessage
import os
months_in_romanian = {
    "Ianuarie": "01",
    "Februarie": "02",
    "Martie": "03",
    "Aprilie": "04",
    "Mai": "05",
    "Iunie": "06",
    "Iulie": "07",
    "August": "08",
    "Septembrie": "09",
    "Octombrie": "10",
    "Noiembrie": "11",
    "Decembrie": "12"
}
data_g = ['Sold', '98,27 lei', '141,76 lei', '15 - 21 Octombrie', '28.08.2020']
data_e = ['', 'Platile efectuate', '1 neachitata', 'Achita factura online', 'Pana pe 14 Oct. 2023', 'Este activata!',
          'Este activat!', '41,49']


def g_text_to_month(data_g: list):
    gaz_splitted = data_g[3].split('-')
    gaz_start_date_day = gaz_splitted[0].strip()
    gaz_end_date_day = gaz_splitted[1].strip().split(' ')[0]
    gaz_month = gaz_splitted[1].strip().split(' ')[-1]

    for i, j in months_in_romanian.items():
        if i == gaz_month:
            gaz_start_date = f"{gaz_start_date_day}/{j}/{datetime.now().strftime('%Y')}"
            gaz_end_date = f"{gaz_end_date_day}/{j}/{datetime.now().strftime('%Y')}"

    return f"{gaz_start_date}-{gaz_end_date}"


def e_text_to_month(data_e: list):
    raw_date_split = data_e[4].split(sep=" ")
    limit_day = raw_date_split[2]
    for i, j in months_in_romanian.items():
        if i.startswith(raw_date_split[3][:3]):
            limit_month = j
    return f"-{limit_day}/{limit_month}/{datetime.now().strftime('%Y')}"


def index_status(date_range):
    date_range = date_range.split('-')

    start_date_str = date_range[0].strip()
    end_date_str = date_range[-1].strip()
    today = datetime.now().today()
    # FOR TEST today = datetime.now().strptime("22/10/2023", '%d/%m/%Y')

    if start_date_str:
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
        if today < start_date:
            return "Perioada auto-citirii nu a început"
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
    if today <= end_date:
        return "În perioada auto-citirii"
    if today > end_date:
        return "Perioada auto-citirii a trecut"

def send_email(user_email, message_raw, gmail_pass):

    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    msg = EmailMessage()
    msg.set_content(message_raw + '\n' + user_email)

    msg['Subject'] = f'New email from {user_email}'
    msg['From'] = user_email
    msg['To'] = "cipi01work@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login("cipi01work@gmail.com", gmail_pass)
        server.send_message(msg)

if __name__ == "__main__":
    send_email('cipriangheorghecapata@gmail.com', 'this is atest')