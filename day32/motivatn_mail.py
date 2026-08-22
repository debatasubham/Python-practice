import smtplib
import datetime as dt
import random

my_email = "lenevosubham@gmail.com"
password = "awdwgzeaxixppams"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("C:/Python practice/day32/quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="debatasubham2020@gmail.com",
            msg=("Subject:Motivational Email\n\n" + quote).encode("utf-8")
        )
