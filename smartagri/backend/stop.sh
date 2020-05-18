ps -ef|awk 'BEGIN{}{if(match($8, /python3/))system("kill -9 " $2)}END{}'

