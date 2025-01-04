from mail_template.data_model import EmailStructure

EMAIL_VERIFY = EmailStructure(
    html_part="""
        <html>
        <head></head>
        <body>
            <h1>Verify Your Email Address!</h1>
            <p>Thank you for signing up! To complete your registration, please verify your email address by entering the code below:</p>
            <h2 style="color: #4CAF50; text-align: center;">{{verification_code}}</h2>
            <p>If you didn't request this email, please ignore it. The code will expire shortly.</p>
            <p>Best regards,<br>The Team</p>
        </body>
        </html>
    """,
    text_part="""
        Verify Your Email Address!

        Thank you for signing up! To complete your registration, please verify your email address by entering the code below:

        Verification Code: {{verification_code}}

        If you didn't request this email, please ignore it. The code will expire shortly.

        Best regards,
        The Team
    """,
)
