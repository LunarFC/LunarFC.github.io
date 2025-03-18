   # app.py
   from flask import Flask, request, redirect, url_for
   from flask_mail import Mail, Message

   app = Flask(__name__)

   # Configure Flask-Mail
   app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your SMTP server
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USE_TLS'] = True
   app.config['MAIL_USERNAME'] = 'harmonyenglishclassesai@gmail.com'  # Replace with your email
   app.config['MAIL_PASSWORD'] = 'harmonyenglishclasses'  # Replace with your email password

   mail = Mail(app)

   @app.route('/submit_form', methods=['POST'])
   def submit_form():
       email = request.form['email']
       mobile = request.form['mobile']
       meeting_date = request.form['meeting_date']
       meeting_time = request.form['meeting_time']

       # Create the email message
       msg = Message('New Contact Form Submission',
                     sender='harmonyenglishclassesai@gmail.com',
                     recipients=['rishi.chaudhary2024@gmail.com'])  # Replace with the recipient's email
       msg.body = f"""
       Email: {email}
       Mobile: {mobile}
       Preferred Meeting Date: {meeting_date}
       Preferred Meeting Time: {meeting_time}
       """

       # Send the email
       mail.send(msg)

       return redirect(url_for('thank_you'))

   @app.route('/thank_you')
   def thank_you():
       return "Thank you for your submission!"

   if __name__ == '__main__':
       app.run(debug=True)