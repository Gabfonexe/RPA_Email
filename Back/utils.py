import openai
from groq import Groq
import os
from dotenv import load_dotenv
import fitz
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import nltk
nltk.download('punkt_tab')         
nltk.download('stopwords')     
nltk.download('wordnet')

load_dotenv()


openai_api_key = os.getenv('groq_api_key')

client =  Groq(api_key=openai_api_key)

def message_classification(message, name):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "Você é um assistente que classifica e-mails como 'Produtivo' ou 'Improdutivo'."},
            {"role": "user", "content": f"Classifique a mensagem abaixo como 'Produtivo' ou 'Improdutivo'. Considere produtivo e-mails que exigem ação ou resposta (ex: solicitações de suporte, dúvidas, atualizações de casos). Considere improdutivo e-mails que não requerem ação imediata (ex: felicitações, agradecimentos), Imporante: Diga somente se é Produtivo ou Improdutivo.\n\nMensagem: \"{message}\""}
        ])
    classification = response.choices[0].message.content.strip()

    return  automatic_message_generate(message, classification, name)


def automatic_message_generate(message, classification, name):

    if classification == "Produtivo":
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
            {"role": "user", "content": f"Você é um atendente profissional. Gere uma resposta clara, educada e objetiva para o e-mail abaixo, abordando a dúvida ou solicitando mais informações se necessário. Ao finalizar a mensagem, coloque sempre o nome da pessoa. Nome da pessoa:{name}. Não esqueça de responder como formato de email. \n\Email: \"{message}\""}
        ])
        data = {'message': response.choices[0].message.content.strip(), 'classification':classification}
        return data
    
    else:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
            {"role": "user", "content": f"Você é um atendente cordial. Gere uma resposta simpática e breve, como agradecimentos ou felicitações. Ao finalizar a mensagem, coloque sempre o nome da pessoa. Nome da pessoa:{name}. Não esqueça de responder como formato de email. \n\Email: \"{message}\""}
        ])

        data = {'message': response.choices[0].message.content.strip(), 'classification':classification}
        return data


def extract_pdf(file):
    text = ""
    file.stream.seek(0) 
    file_bytes = file.read()
    with fitz.open(stream=file_bytes, filetype="pdf") as pdf:
        for page in pdf:
            text += page.get_text()
    return text

    
def extract_txt(file):
    file.stream.seek(0)
    return file.read().decode('utf-8')


def preprocess_text(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [t for t in tokens if t not in string.punctuation]

    stop_words = set(stopwords.words('portuguese')) 
    tokens = [t for t in tokens if t not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return ' '.join(tokens)

