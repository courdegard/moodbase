from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pathlib import Path
from dotenv import load_dotenv
load_dotenv('.env')
from decouple import config

# environment variables
class Envs:
    MAIL_USERNAME = config('MAIL_USERNAME')
    MAIL_PASSWORD = config('MAIL_PASSWORD')
    MAIL_FROM = config('MAIL_FROM')
    MAIL_PORT = int(config('MAIL_PORT'))
    MAIL_SERVER = config('MAIL_SERVER')
    MAIL_FROM_NAME = config('MAIL_FROM_NAME')

# mail config

mailer = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT,
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    # TEMPLATE_FOLDER=Path(__file__).parent.parent / "templates"
)

# mail functions

async def send_email_async(emailSpecs):
    recipient="danbidikov@gmail.com"
    # template_body={'url':url}
    message = MessageSchema(
        subject=emailSpecs['subject'],
        recipients=[recipient],
        template_body=emailSpecs['urlDict'],
        subtype='html',
    )
    
    fm = FastMail(mailer)
    await fm.send_message(message,template_name=emailSpecs['template'])

async def sendEmailBackground(emailSpecs:dict):
    recipient="danbidikov@gmail.com"
    message = MessageSchema(
        subject=emailSpecs['subject'],
        recipients=[recipient],
        template_body=emailSpecs['urlDict'],
        subtype='html',
    )
    # background_task=BackgroundTasks
    fm = FastMail(mailer)
    await fm.send_message( message, template_name=emailSpecs['template'])

    # return {'message':'email has been sent'}