from textwrap import dedent
from mail_template.data_model import EmailStructure

EMAIL_VERIFY = EmailStructure(
    html_part=dedent("""
        <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .container {
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 30px;
            margin: 20px 0;
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #f0f0f0;
            margin-bottom: 20px;
        }
        .title {
            color: #2563eb;
            font-size: 24px;
            margin: 0;
            padding: 0;
        }
        .verification-code {
            background-color: #f8fafc;
            border-radius: 6px;
            padding: 20px;
            margin: 25px 0;
            text-align: center;
        }
        .code {
            font-family: monospace;
            font-size: 32px;
            letter-spacing: 4px;
            color: #1e40af;
            margin: 0;
            padding: 10px;
        }
        .instructions {
            color: #4b5563;
            font-size: 16px;
            margin: 20px 0;
        }
        .expiry {
            color: #dc2626;
            font-size: 14px;
            margin-top: 15px;
        }
        .footer {
            text-align: center;
            color: #6b7280;
            font-size: 14px;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #f0f0f0;
        }
        .help {
            background-color: #f8fafc;
            border-left: 4px solid #2563eb;
            padding: 15px;
            margin: 20px 0;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="title">Welcome to {{company_name}}!</h1>
        </div>

        <div class="instructions">
            <p>Hi{{#if name}} {{name}}{{/if}},</p>
            <p>Thanks for signing up! To ensure the security of your account, please verify your email address using the code below:</p>
        </div>

        <div class="verification-code">
            <h2 class="code">{{verification_code}}</h2>
            <p class="expiry">This code will expire in {{expiry_time}} minutes</p>
        </div>

        <div class="help">
            <p><strong>Need help?</strong> If you're having trouble verifying your email, please contact our support team at {{support_email}}</p>
        </div>

        <div class="footer">
            <p>This email was sent to {{user_email}}.</p>
            <p>If you didn't create an account with {{company_name}}, please ignore this email or contact us if you have concerns.</p>
            <p>&copy; {{current_year}} {{company_name}}. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
    """).strip(),
    text_part=dedent("""
Welcome to {{company_name}}!

Hi{{#if name}} {{name}}{{/if}},

Thanks for signing up! To ensure the security of your account, please verify your email address using the code below:

Your verification code: {{verification_code}}

This code will expire in {{expiry_time}} minutes.

Need help? If you're having trouble verifying your email, please contact our support team at {{support_email}}

This email was sent to {{user_email}}.
If you didn't create an account with {{company_name}}, please ignore this email or contact us if you have concerns.

© {{current_year}} {{company_name}}. All rights reserved.
    """).strip(),
)
