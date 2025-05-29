import tkinter as tk
from tkinter import filedialog, messagebox
from email.message import EmailMessage
import smtplib
import os
import datetime
import locale
import re
import mimetypes

# Define localidade para datas em português
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
except:
    locale.setlocale(locale.LC_TIME, 'portuguese')

# Saudação de acordo com a hora do dia
def saudacao_do_dia():
    hora = datetime.datetime.now().hour
    if 5 <= hora < 12:
        return "Bom dia"
    elif 12 <= hora < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

# Função para enviar o e-mail
def enviar_email():
    email_destino = entry_email.get()
    assunto = entry_assunto.get()
    caminho_arquivo = entry_arquivo.get()

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_destino):
        messagebox.showerror("Erro", "E-mail inválido.")
        return

    if not os.path.exists(caminho_arquivo):
        messagebox.showerror("Erro", "Arquivo não encontrado.")
        return

    caminho_imagem = 'C:/Cursos_Python/envio_email_automatico/Email Automatico/envio_emails_python/background.png'
    if not os.path.exists(caminho_imagem):
        messagebox.showerror("Erro", "Imagem para e-mail não encontrada.")
        return
    


    data_formatada = datetime.datetime.now().strftime("%d de %B de %Y")
    saudacao = saudacao_do_dia()

    # Corpo HTML com imagem inline
    html = f'''
    <html>
      <body style="font-family: Arial; padding: 10px;">
        <h3>{saudacao}, tudo bem?</h3>
        <p>Segue em anexo o meu currículo atualizado.</p>
        <p>Enviado automaticamente em {data_formatada}.</p>
        <br>
        <img src="cid:logo_python" alt="Python Logo" style="width: 50px; height: auto;">
        <p style="font-size: 12px; color: gray;">Este e-mail foi gerado com Python</p>   
        </a>
    </html>
    '''

    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = 'rf@gmail.com'
    msg['To'] = email_destino
    msg.set_content("Segue o currículo em anexo.\n\nAtenciosamente,\nRafael Da Silva")
    msg.add_alternative(html, subtype='html')

    # Anexar currículo PDF
    with open(caminho_arquivo, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=os.path.basename(caminho_arquivo))

    # Anexar imagem inline
    with open(caminho_imagem, 'rb') as img:
        img_data = img.read()
        maintype, subtype = mimetypes.guess_type(caminho_imagem)[0].split('/')
        msg.get_payload()[1].add_related(img_data, maintype=maintype, subtype=subtype, cid='logo_python')


    # Envio do e-mail
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('rf@gmail.com', '*******************')  
            smtp.send_message(msg)
            messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar e-mail:\n{e}")

# Função para selecionar o PDF
def selecionar_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    entry_arquivo.delete(0, tk.END)
    entry_arquivo.insert(0, caminho)

# Interface Gráfica
janela = tk.Tk()
janela.title("Envio de Currículo por E-mail")
janela.geometry("500x250")

tk.Label(janela, text="E-mail destino:").pack(pady=2)
entry_email = tk.Entry(janela, width=60)
entry_email.pack()

tk.Label(janela, text="Assunto do e-mail:").pack(pady=2)
entry_assunto = tk.Entry(janela, width=60)
entry_assunto.insert(0, "Rafael - Currículo")
entry_assunto.pack()

tk.Label(janela, text="Selecionar arquivo PDF:").pack(pady=2)

frame_arquivo = tk.Frame(janela)
frame_arquivo.pack(pady=5)
entry_arquivo = tk.Entry(frame_arquivo, width=50)
entry_arquivo.pack(side=tk.LEFT, padx=10)
btn_arquivo = tk.Button(frame_arquivo, text="Procurar", command=selecionar_arquivo)
btn_arquivo.pack(side=tk.LEFT)

tk.Button(janela, text="Enviar E-mail", command=enviar_email, bg="green", fg="white").pack(pady=20)

janela.mainloop()
