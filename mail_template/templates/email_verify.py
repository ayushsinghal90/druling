from mail_template.data_model import EmailStructure

EMAIL_VERIFY = EmailStructure(
    html_part="""
                <html>
                <head></head>
                <body>
                    <h1>Welcome to {{company_name}}!</h1>
                    <p>Hello {{name}},</p>
                    <p>We're excited to have you on board. Here are some things you can do to get started:</p>
                    <ul>
                        <li>Complete your profile</li>
                        <li>Explore our features</li>
                        <li>Connect with others</li>
                    </ul>
                    <p>If you have any questions, don't hesitate to reach out to our support team.</p>
                    <p>Best regards,<br>The {{company_name}} Team</p>
                </body>
                </html>
                """,
    text_part="""
                Welcome to {{company_name}}!

                Hello {{name}},

                We're excited to have you on board. Here are some things you can do to get started:
                - Complete your profile
                - Explore our features
                - Connect with others

                If you have any questions, don't hesitate to reach out to our support team.

                Best regards,
                The {{company_name}} Team
                """,
)
