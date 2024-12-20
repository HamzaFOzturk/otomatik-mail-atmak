import smtplib
from email.mime.text import MIMEText
smtp_server = "smtp@gmail.com"
smtp_port = 587 
email_address = "hamzafazlikadirozturk@gmail.com"
email_password = "Sabah2020"
recipients = ["schneider.turkiye@schneider-electric.com", 
              "info@assanhanil.com.tr", 
              "info@arcelik.com.tr", 
              "info@gubretas.com.tr"]
subject = "teknik gezi hk."
body = """

Merhaba
ben Hamza Fazli Kadir Ozturk, Kocaeli Universitesi Makine Muhendisligi Kulubu Sosyal Sorumluluk ve Teknik Gezi Koordinatoruyum,
MMK olarak muhendis ögrencilerini sektore hazýrlamak amaciyla kulubumuz okulumuzun en buyuk teknik takimlari ile
Amerika'da Avrupa'da ; yurt ici ve disi bir cok yarismada gurulandiriyor
ancak bir muhendsilik ögrencisini sektore hazirlamak icin sadece teknik bilgi yetmiyor bunun yanýnda sektor bilgiside
gerekiyor, bu nedenle kulubumuz sizinle is birligi yapmak isityor;

Gezi hakkinda detayli bilgi almak ve uygun tarihleri belirlemek adina geri donuslerinizi bekliyorum.

Ilginize tesekkur ederim.

Saygilarimla,
Hamza Ozturk" 

"""
for recipient in recipients:
    msg = MIMEText(body)
    msg["From"] = email_address
    msg["To"] = recipient
    msg["Subject"] = subject

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.sendmail(email_address, recipient, msg.as_string())
        print(f"Mail gönderildi: {recipient}")
    except Exception as e:
        print(f"Mail gönderilemedi: {recipient}, Hata: {e}")