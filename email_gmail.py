import smtplib
from email.message import EmailMessage
import os

# Caminho do arquivo
caminho_arquivo = r"C:\Cursos_Python\Email Automatico\envio_emails_python\CurriculoMaio2025.pdf"

# Verifica se o arquivo existe
if not os.path.exists(caminho_arquivo):
    print(f"ERRO: Arquivo não encontrado:\n{caminho_arquivo}")
    exit(1)

# Cria a mensagem de e-mail
msg = EmailMessage()
msg['Subject'] = 'Rafael, Currículo'
msg['From'] = 'rsilva@gmail.com'
msg['To'] = 'rsilva@gmail.com'
msg.set_content(
    "Olá, Jivago. Tudo bem?\n\nSegue meu currículo em anexo.\n\nDesde já, Obrigado!\nRafael Da Silva"
)

# Lê o arquivo PDF e anexa ao e-mail
with open(caminho_arquivo, 'rb') as f:
    file_data = f.read()
    file_name = "Curriculo_Rafael.pdf"
    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

# Tenta enviar o e-mail
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('rfsrafaelsilva@gmail.com', 'beat cgxo bfql dzaw')  # senha de app
        smtp.send_message(msg)
        print("E-mail enviado com sucesso!")
except Exception as e:
    print("ERRO ao enviar o e-mail:")
    print(e)
finally:
    print("Finalizando o script.")
