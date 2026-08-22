# email SMTP - simple mail transfer protocol
# daytime
import smtplib

my_email = "lenevosubham@gmail.com"
password = "awdwgzeaxixppams"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="debatasubham2020@gmail.com",
        msg="Subject:Hello\n\nThis message is only for checking the automatic email working or not"
    )

