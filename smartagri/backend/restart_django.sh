ps -ef|awk 'BEGIN{}{if(match($8, /python3/))system("kill -9 " $2)}END{}'
nohup python3 manage.py runserver 0.0.0.0:8888 >djo.out 2>&1 &
