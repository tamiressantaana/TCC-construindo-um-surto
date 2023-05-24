#Importando a biblioteca feedparser para fazer a leitura das notícias do feed RSS
#Importando smtplib para configurar envio de emails
#Importando MIMEText para criar o conteúdo do email 
import feedparser
import smtplib
from email.mime.text import MIMEText

#Definindo as configurações do email, basicamente, remetente, destinatário, configurações do servidor smtp e autenticação
email_from = 'seu_email@gmail.com'
email_to = 'destinatario@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'seu_email@gmail.com'
smtp_password = 'sua_senha'

#Depositando o URL do RSS 
feed_url = 'URL_DO_FEED'

#fazendo parser do feed e armazenando na variável feed
feed = feedparser.parse(feed_url)

#Checando se atualização com a função published_parsed que compara os dados de publicação das últimas entradas com as novas
if 'published_parsed' in feed.feed:
    last_checked = feed.feed.published_parsed
else:
    last_checked = None

#Criando uma lista vazia para guardar as novas entradas (atualizações do feed)
new_entries = []

#Iterando sobre as novas entradas no feed com a função 'feed.entries'
#entry = cada entrada do feed em cada iteração
#No if verifico se 'last_checked' (ultima checagem) é None ou se a data de publicação de 'entry.published_parsed' é maior que o horário da última verificação feita (last_checked)
#Se alguma das condições for verdadeiras, a entrada é uma nova atualização do feed, então é adiciono em 'new_entries' 
for entry in feed.entries:
    if last_checked is None or entry.published_parsed > last_checked:
        new_entries.append(entry)


if new_entries: #se houver atualizações
    subject = 'Houve nova atualização no feed RSS ' #Define o assunto do email
    body = '' #string vazia para gyardar o conteúdo do email

    for entry in new_entries: #iterando sobre cada entrada na lista 'new_entries'
        body += f'Título: {entry.title}\n' #adicionando o título do email
        body += f'Link: {entry.link}\n' #adicionando o link da nova notícia
        body += f'Resumo: {entry.summary}\n' #adicionando um resumo da notícia
        body += '---\n' #quebrando uma linha a cada entrada nova

    msg = MIMEText(body) #criando um corpo de email em formato de texto
    msg['Assunto'] = subject #definindo que o assunto será o 'subject' definido anteriormente
    msg['De'] = email_from #definindo o rementente
    msg['Para'] = email_to #definindo o destinatário

    server = smtplib.SMTP(smtp_server, smtp_port) #iniciando conexão com servidor smtp
    server.starttls() #chamando 'starttls()' para estabelecer conexão segura TLS
    server.login(smtp_username, smtp_password) #credenciais de acesso ao servidor
    server.sendmail(email_from, email_to, msg.as_string()) #enviando os emails
    server.quit() #Encerrando conexão com o servidor
