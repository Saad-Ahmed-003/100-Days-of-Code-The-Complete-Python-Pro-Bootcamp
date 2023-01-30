import smtplib

my_email = "saadbinsajid03@gmail.com"
password = "rausxdgvtjyofmcc"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="learn.saad.dev03@gmail.com", msg="Subject:hi\n\nbody")
connection.close()

