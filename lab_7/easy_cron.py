import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sender_email = 'sender@gmail.com'
receiver_email = 'receiver@outlook.com'
password_of_sender = 'thisIsOnlyForExample'
smtp_server = 'smtp.example.com'
smtp_port = 465

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'This is a test email'

body_content = '''This purely numerical and social superiority is not the only fact concerned. Added
to it is a more internal consideration: Nonnarrative films for the most part are dis-
tinguished from “real” films by their social purpose and by their content much more
than by their “language processes.” The basic figures of the semiotics of the cin-
ema—montage, camera movements, scale of the shots, relationships between the
image and speech, sequences, and other large syntagmatic units—are on the whole
the same in “small” films and in “big” films. It is by no means certain that an inde-
pendent semiotics of the various nonnarrative genres is possible other than in the
form of a series of discontinuous remarks on the points of difference between these
films and “ordinary” films. To examine fiction films is to proceed more directly and
more rapidly to the heart of the problem.
There is, moreover, an encouraging diachronic consideration. We know, since the
observations of Béla Balázs, André Malraux, Edgar Morin, Jean Mitry, and many
others, that the cinema was not a specific “language” from its inception. Before
becoming the means of expression familiar to us, it was a simple means of mechan-
ical recording, preserving, and reproducing moving visual spectacles—whether of
life, of the theater, or even of small mises-en-scène, which were specially prepared
and which, in the final analysis, remained theatrical—in short, a “means of repro-
duction,” to use André Malraux’s term. Now, it was precisely to the extent that the
cinema confronted the problems of narration that, in the course of successive group-
ings, it came to produce a body of specific signifying procedures. Historians of the
cinema generally agree in dating the beginning of the cinema as we know it in the
period 1910–15. Films like Enoch Arden, Life for the Czar, Quo Vadis?, Fantômas,
Cabiria, The Golem, The Battle of Gettysburg, and above all Birth of a Nation were
among the first films, in the acceptation we now give this word when we use it with-
out a determinant: Narration of a certain magnitude based on procedures that are
supposed to be specifically cinematographic. It so happens that these procedures
were perfected in the wake of the narrative endeavor. The pioneers of “cinemato-
graphic language”—Méliès, Porter, Griffith—couldn’t care less about “formal”
research conducted for its own sake; what is more (except for occasional naïve and
confused attempts), they cared little about the symbolic, philosophical, or human
“message” of their films. Men of denotation rather than of connotation, they wanted
above all to tell a story; they were not content unless they could subject the con-
tinuous, analogical material of photographic duplic'''

body = MIMEText(body_content, 'plain', "utf-8")
message.attach(body)

with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender_email, password_of_sender)
    server.send_message(message)
