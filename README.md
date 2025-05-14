Envio de E-mail Automático com Python
Este repositório contém três scripts Python para enviar e-mails automáticos através do Outlook e SMTP, com a possibilidade de personalizar o corpo da mensagem, anexar arquivos e definir saudações dinâmicas com base no horário.

Arquivos do Repositório
1. email_gmail.py
Este script é responsável por enviar um e-mail utilizando o serviço SMTP do Gmail. Ele permite o envio de e-mails com texto simples e anexos (como PDFs).

2. email_outlook.py
Este script utiliza o Microsoft Outlook para enviar e-mails diretamente. Ele inclui uma saudação personalizada com base no horário atual e formatação de HTML no corpo da mensagem.

3. envio_email.ipynb
Notebook Jupyter que pode ser utilizado para experimentar e rodar o envio de e-mails com base no conteúdo dos dois scripts anteriores. Ele também facilita o teste em ambiente interativo.

Como Usar
Pré-requisitos
Python 3.x instalado em sua máquina.

Microsoft Outlook instalado e configurado no seu computador (para o script email_outlook.py).

Conta do Gmail configurada para permitir acesso a aplicativos menos seguros (para o script email_gmail.py).

Bibliotecas adicionais que podem ser necessárias:

win32com.client (para interação com o Outlook).

smtplib e email.message (para envio de e-mails via Gmail).

datetime, locale (para manipulação de data e hora).

Passo a Passo
1. email_gmail.py
Este script envia e-mails através do Gmail. Você precisa configurar a conta do Gmail e, caso o acesso esteja restrito, ativar a opção para permitir "Aplicativos Menos Seguros" nas configurações da sua conta do Google.

bash
Copiar
Editar
python email_gmail.py
2. email_outlook.py
Este script envia e-mails usando o Outlook, utilizando a biblioteca win32com.client para criar e enviar mensagens. Ele inclui uma saudação dinâmica (Bom dia, Boa tarde, Boa noite), dependendo da hora do dia.

Certifique-se de ter o Outlook instalado e configurado corretamente em sua máquina para que o script funcione.

bash
Copiar
Editar
python email_outlook.py
3. envio_email.ipynb
Se você estiver usando o Jupyter Notebook, pode utilizar este notebook interativo para experimentar os dois scripts acima. Basta executar as células do notebook conforme necessário.

Abra o notebook:

bash
Copiar
Editar
jupyter notebook envio_email.ipynb
Personalizações
Saudações Dinâmicas: No script email_outlook.py, o corpo do e-mail é personalizado com uma saudação baseada na hora atual. A saudação pode ser "Bom dia", "Boa tarde" ou "Boa noite", dependendo da hora em que o e-mail for enviado.

Corpo do E-mail em HTML: O corpo do e-mail é configurado usando HTML, permitindo que você personalize a formatação, como cores, fontes e links.

Anexar Arquivos: Os arquivos podem ser anexados aos e-mails alterando o caminho do arquivo na variável Local_Arquivo (nos scripts email_outlook.py e email_gmail.py).

Exemplos de Uso
Exemplo de E-mail do Outlook (email_outlook.py)
Envio de e-mail com saudação dinâmica:

python
Copiar
Editar
Email.To = 'destinatario@example.com'
Email.Subject = 'Assunto do E-mail'
Email.Body = 'Mensagem no corpo do e-mail.'
Email.HTMLBody = '<html><body>Saudação e conteúdo em HTML.</body></html>'
Exemplo de E-mail do Gmail (email_gmail.py)
Envio de e-mail com anexo:

python
Copiar
Editar
msg['To'] = 'destinatario@example.com'
msg['From'] = 'seu_email@gmail.com'
msg.set_content('Mensagem do corpo do e-mail.')

with open("caminho/do/arquivo.pdf", 'rb') as f:
    file_data = f.read()
    file_name = "Arquivo_PDF.pdf"

msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

# Enviar o e-mail via Gmail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('seu_email@gmail.com', 'sua_senha')
    smtp.send_message(msg)
Contribuindo
Sinta-se à vontade para contribuir para este repositório, enviando um pull request com melhorias ou correções.

Como Usar o Agendador de Tarefas do Windows para Agendar Execuções
O Agendador de Tarefas do Windows permite que você execute programas ou scripts em horários específicos ou quando certos eventos ocorrerem. Aqui está um guia passo a passo com imagens para ajudá-lo a configurar o agendamento de tarefas.

Passo 1: Abrir o Agendador de Tarefas
No menu de Iniciar, digite "Agendador de Tarefas" ou "Task Scheduler".

Clique em Agendador de Tarefas para abrir o programa.


Passo 2: Criar uma Nova Tarefa
No painel à direita, clique em Criar Tarefa.


Passo 3: Definir as Informações Gerais
Na aba Geral, dê um nome à tarefa e, se necessário, forneça uma descrição.

Nome: Dê um nome intuitivo para a tarefa (por exemplo, "Execução do Script Python").

Descrição: (opcional) Escreva uma descrição da tarefa.

Se quiser que a tarefa seja executada mesmo quando o usuário não estiver logado, marque a opção Executar com privilégios mais altos.


Passo 4: Configurar o Agendamento
Vá até a aba Triggers (Gatilhos) e clique em Novo.


Escolha o tipo de gatilho que você deseja:

Diariamente: Se você quiser que o script seja executado todos os dias.

Semanalmente: Se você quiser definir um horário fixo semanal para a execução.

Ao iniciar o computador: Se você quiser que o script seja executado sempre que o computador for ligado.

Configure a hora e a frequência conforme desejado e clique em OK.


Passo 5: Definir a Ação
Vá até a aba Ações e clique em Novo.


No campo Ação, selecione Iniciar um programa.

Clique em Procurar e selecione o script que você deseja executar (por exemplo, seu arquivo .py ou .bat).

Se você estiver executando um script Python, na caixa Programa/script, insira o caminho do interpretador Python, como C:\Python39\python.exe e, no campo Adicionar argumentos, adicione o caminho do seu script Python.

Exemplo:

Programa/script: C:\Python39\python.exe

Adicionar argumentos: C:\Caminho\para\seu_script.py

Clique em OK.


Passo 6: Configurações Avançadas (Opcional)
Na aba Configurações, você pode ajustar a tarefa para garantir que ela seja executada corretamente, mesmo se o computador estiver em modo de economia de energia ou se a tarefa falhar.

Marque a opção Parar a tarefa se ela durar mais de para limitar o tempo máximo de execução da tarefa, se necessário.

Após configurar as opções desejadas, clique em OK.


Passo 7: Finalizar e Testar
Clique em OK para salvar a tarefa.

Para testar se a tarefa está configurada corretamente, selecione a tarefa na lista e clique em Executar no painel à direita.


Agora você configurou com sucesso uma tarefa agendada no Windows para executar automaticamente seu script Python ou outro programa na hora e data que você configurou.

Dicas Finais
Verifique se o script funciona: Antes de agendar a tarefa, sempre execute seu script manualmente para garantir que ele funcione corretamente.

Verifique permissões: Certifique-se de que você tem as permissões adequadas para executar o script, especialmente se ele interagir com arquivos ou recursos do sistema.

Agora, o Agendador de Tarefas irá cuidar do resto, executando o script no horário determinado!

Espero que esse guia com imagens tenha sido útil! Se precisar de mais alguma ajuda ou quiser ajustar algo, fique à vontade para perguntar.


