#!/usr/bin/env python
# coding: utf-8

# Importando as bibliotecas
import win32com.client as win32
import datetime
import locale

# Configurando a localidade para português
locale.setlocale(locale.LC_TIME, 'portuguese')

# Pegando a hora atual
agora = datetime.datetime.now()
hora = agora.hour

# Pegando a data atual formatada (ex: 10 de abril de 2025)
agora_data = datetime.datetime.today().strftime("%d de %B de %Y")

# Definindo a saudação com base na hora
if 5 <= hora < 12:
    saudacao = "Bom dia"
elif 12 <= hora < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

# Instanciando o aplicativo Outlook
Outlook = win32.Dispatch('outlook.application')

# Criando o e-mail
Email = Outlook.CreateItem(0)
Email.To = 'taiscmoreira@icloud.com'
Email.CC = 'rfsrafaelsilva@gmail.com'
Email.Subject = 'IRPF Camila Andrigui'
Email.Body = 'Message body'



# Corpo do e-mail com saudação dinâmica

html = f'''
<html>
  <head>
    <meta charset="UTF-8">
    <style>
      body {{
        background-image: url('https://www.transparenttextures.com/patterns/white-wall-3.png'); /* imagem de fundo leve */
        background-repeat: repeat;
        background-size: auto;
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
      h2, h3 {{
        color: #111;
      }}
      .highlight {{
        background-color: #000;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
      }}
      .social-icons {{
        margin-top: 20px;
        text-align: center;
      }}
      .social-icons img {{
        width: 24px;
        height: 24px;
        margin: 0 10px;
        vertical-align: middle;
      }}
      a {{
        color: #0073b1;
        text-decoration: none;
      }}
      a:hover {{
        text-decoration: underline;
      }}
      ul {{
        padding-left: 20px;
      }}
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
      <div>
        <h2>Sou seu e-mail automático</h2>
        <p>
          Estou passando para te lembrar que você tem que imprimir a guia de pagamento 
          de IRPF 2025 de Camila Andrigui.
        </p>
      </div>
      <div class="footer">
        <p>Este e-mail foi enviado automaticamente com Python 🐍</p>
      </div>

    </div>
  </body>
</html>
'''

# Aplicando HTML no seu e-mail
Email.HTMLBody = html

# Enviar e-mail
Email.Send()

print("E-mail enviado com sucesso!") 