docker build -t app ./app/
docker build -t app/logstash ./logstash/
#docker build -t app/nginx ./nginx/
docker-compose up -d
