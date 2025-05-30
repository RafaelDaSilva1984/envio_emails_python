import tkinter as tk
from tkinter import filedialog, messagebox
from email.message import EmailMessage
import smtplib
import os
import datetime
import locale
import re
import mimetypes


# Configura o locale para datas em português
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
except:
    locale.setlocale(locale.LC_TIME, 'portuguese')

# Saudação baseada na hora do dia
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
    email_destino = entry_email.get().strip()
    assunto = entry_assunto.get().strip()
    caminho_arquivo = entry_arquivo.get().strip()

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_destino):
        messagebox.showerror("Erro", "E-mail inválido.")
        return

    if not os.path.exists(caminho_arquivo):
        messagebox.showerror("Erro", "Arquivo não encontrado.")
        return

    # CIDs e caminhos das imagens inline
    imagens = {
        'logo_python': 'C:/Cursos_Python/envio_email_automatico/Email Automatico/envio_emails_python/background.png',
        'logo_linkedin': 'C:/Cursos_Python/envio_email_automatico/Email Automatico/envio_emails_python/linkedin.png',
        'logo_github': 'C:/Cursos_Python/envio_email_automatico/Email Automatico/envio_emails_python/github.png',
        'logo_watsapp': 'C:/Cursos_Python/envio_email_automatico/Email Automatico/envio_emails_python/whatsapp.png'
    }

    # Verificação de existência das imagens
    for cid, caminho in imagens.items():
        if not os.path.exists(caminho):
            messagebox.showerror("Erro", f"Imagem '{cid}' não encontrada.")
            return

    data_formatada = datetime.datetime.now().strftime("%d de %B de %Y")
    saudacao = saudacao_do_dia()

    # Corpo HTML
    html = f'''
    <html>
      <body style="font-family: Arial; padding: 10px;">
        <h3>{saudacao}, tudo bem?</h3>
        <p>Segue em anexo o meu currículo atualizado.</p>
        <p>Enviado automaticamente em {data_formatada}.</p>
        <br>          
        <img src="cid:logo_linkedin" alt="LinkedIn Logo" style="width: 20px; height: auto;">
             <a href="https://www.linkedin.com/in/rafael-da-silva-rfs-desenvolvedor/" target="_blank">LinkedIn</a>    
             <br><br>    
        <img src="cid:logo_github" alt="GitHub Logo" style="width: 20px; height: auto;"> 
            <a href="https://github.com/RafaelDaSilva1984" target="_blank">Github</a>    
             <br><br>    
       <img src="cid:logo_watsapp" alt="WhatsApp Logo" style="width: 20px; height: auto;" <p style="font-size: 12px; color: gray;">
                Entre em contato comigo pelo WhatsApp - (54)9-9677-2904</p>        
             <!--<a href="https://api.whatsapp.com/send?phone=5511111111111" target="_blank">WhatsApp</a> -->
             <br><br>
       <img src="cid:logo_python" alt="Python Logo" style="width: 50px; height: auto;">
            <p style="font-size: 12px; color: gray;">Este e-mail foi gerado com Python</p>
    </html>
    '''

    # Criação da mensagem
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = 'raffa@gmail.com'
    msg['To'] = email_destino
    msg.set_content("Segue o currículo em anexo.\n\nAtenciosamente,\nRafael")
    msg.add_alternative(html, subtype='html')

    # Anexar PDF
    with open(caminho_arquivo, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=os.path.basename(caminho_arquivo))

    # Adicionar imagens inline
    for cid, caminho in imagens.items():
        with open(caminho, 'rb') as img:
            img_data = img.read()
            maintype, subtype = mimetypes.guess_type(caminho)[0].split('/')
            msg.get_payload()[1].add_related(img_data, maintype=maintype, subtype=subtype, cid=cid)

    # Enviar o e-mail
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('raffa@gmail.com', '**** **** **** ****')  #IMPORTANTE: use app password
            smtp.send_message(msg)
            messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar e-mail:\n{e}")

# Função para escolher o arquivo
def selecionar_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    entry_arquivo.delete(0, tk.END)
    entry_arquivo.insert(0, caminho)

# Interface gráfica
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
