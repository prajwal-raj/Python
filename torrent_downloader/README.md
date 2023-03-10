# Controlling Your Computer Through Email

This program is designed to be scheduled at a regular interval (e.g., every 20 minutes). When run, the script checks an email's inbox for any instructions and executes any matches automatically. For example, BitTorrent is a peer-to-peer downloading system. Using free BitTorrent software such as qBittorrent, you can download large media files on your home computer. If you email the program a (completely legal, not at all piratical) BitTorrent link, the program will eventually check its email, find this message, extract the link, and then launch qBittorrent to start downloading the file. This way, you can have your home computer begin downloads while you’re away, and the (completely legal, not at all piratical) download can be finished by the time you return home.

Of course, you’ll want the program to make sure the emails come from you. In particular, you might want to require that the emails contain a password, since it is fairly trivial for hackers to fake a “from” address in emails. The program should delete the emails it finds so that it doesn’t repeat instructions every time it checks the email account. As an extra feature, have the program email or text you a confirmation every time it executes a command.

## Sample Instructional Email
<p align=center>
  <img src=./images/sample_instructional_email.png alt=sample instructional email>
</p>

## Sample Notification
<p align=center>
  <img src=./images/sample_notification.jpeg alt=sample notification message height=300>
</p>
