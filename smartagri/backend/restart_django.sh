echo $(date)" restart django server"
ps -ef|awk 'BEGIN{}{if(match($8, /python3/))system("kill -9 " $2)}END{}'
nohup python3 /home/ubuntu/SmartAgri/smartagri/backend/manage.py runserver 0.0.0.0:8888 >/home/ubuntu/SmartAgri/smartagri/backend/logs/django_out.log 2>&1 &
