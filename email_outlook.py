#!/usr/bin/env python
# coding: utf-8

# Importando bibliotecas
import win32com.client as win32
import datetime
import locale
import pywhatkit  # WhatsApp

# Configura localidade para datas em português
locale.setlocale(locale.LC_TIME, 'portuguese')

# Hora e data atual
agora = datetime.datetime.now()
hora = agora.hour
agora_data = agora.strftime("%d de %B de %Y")

# Saudação automática
if 5 <= hora < 12:
    saudacao = "Bom dia"
elif 12 <= hora < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

# ======= EMAIL =======

# Instanciando o Outlook e criando o e-mail
Outlook = win32.Dispatch('outlook.application')
Email = Outlook.CreateItem(0)
Email.To = 'taiscmoreira@icloud.com'
Email.CC = 'rfsrafaelsilva@gmail.com'
Email.Subject = 'IRPF Camila Andrigui'
Email.Body = 'Mensagem automática'

# Corpo HTML do e-mail
html = f'''
<html>
  <head>
    <meta charset="UTF-8">
    <style>
      body {{
        background-image: url('https://www.transparenttextures.com/patterns/white-wall-3.png');
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333;
        padding: 20px;
      }}
      .container {{
        max-width: 600px;
        margin: auto;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        padding: 30px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
      }}
      h2, h3 {{ color: #111; }}
      .footer {{
        text-align: center;
        font-size: 12px;
        color: #666;
        margin-top: 30px;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <h3>{saudacao} 👋</h3>
      <h2>Sou seu e-mail automático</h2>
      <p>
        Estou passando para te lembrar que você tem que imprimir a guia de pagamento 
        de IRPF 2025 de Camila Andrigui.
      </p>
      <div class="footer">
        <p>Este e-mail foi enviado automaticamente com Python 🐍</p>
      </div>
    </div>
  </body>
</html>
'''

# Aplicando HTML e enviando
Email.HTMLBody = html
Email.Send()
print("✅ E-mail enviado com sucesso!")

# ======= WHATSAPP =======

# Número no formato internacional (Brasil: +55 + DDD + número)
numero_destino = "+5554999182644"

# Mensagem de WhatsApp
mensagem = f"""{saudacao}! 👋
Lembrete automático: Não esqueça de imprimir a guia de pagamento do IRPF 2025 da Camila Andrigui.
(Este aviso foi enviado via Python 🐍)
"""

# Enviando mensagem instantaneamente
pywhatkit.sendwhatmsg_instantly(numero_destino, mensagem, wait_time=15, tab_close=True)

print("✅ Mensagem enviada no WhatsApp com sucesso!")
