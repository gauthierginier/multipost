echo "Création du dossier .ssh s'il n'existe pas déjà"
ssh gogodev@192.168.1.63 "mkdir .ssh"

echo "Copier la clé public du poste vers le serveur"
scp C:\\Users\utilisateur\.ssh\id_rsa.pub gogodev@192.168.1.63:./.ssh/authorized_keys

echo "Désactive l'authentification par mot de passe du SSH"
ssh gogodev@192.168.1.63 "sed 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config"

echo "Déployer script.sh"
scp  C:\\Users\utilisateur\Desktop\simplon\multipost\post-install2.sh gogodev@192.168.1.63:./script.sh
scp  C:\\Users\utilisateur\Desktop\simplon\multipost\file.sql gogodev@192.168.1.63:./file.sql

ssh gogodev@192.168.1.63 "chmod 777 ./script.sh"
ssh gogodev@192.168.1.63 "chmod 777 ./file.sql"
pip install mysql-connector-python
ssh -t gogodev@192.168.1.63 "sudo -S ./script.sh"
