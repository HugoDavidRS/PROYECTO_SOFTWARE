from flask_mail import Message
from flask import current_app
from src.common.vars import HOME_HOST


class EmailService:
    def __init__(self):
        pass

    def send_approval_email(self, user_email: str, file_id: str, filename: str):
        """Enviar un correo con el enlace de aprobación para el archivo."""
        try:
            mail = current_app.mail

            approve_url = f"http://localhost:{HOME_HOST}/approve/{file_id}"

            subject = "Aprobación requerida: archivo para firmar"
            html_body = f"""
            <p>Hola,</p>
            <p>Se ha subido el archivo <strong>{filename}</strong> y requiere aprobación.</p>
            <p>Haga click en el siguiente enlace para aprobar y firmar el archivo:</p>
            <p><a href=\"{approve_url}\">Aprobar archivo</a></p>
            <p>Si no esperaba este correo, puede ignorarlo.</p>
            """

            msg = Message(subject=subject, recipients=[user_email], html=html_body)
            mail.send(msg)
            print(f"Email enviado a {user_email} con enlace {approve_url}")
        except Exception as e:
            print(f"Error enviando correo: {e}")
