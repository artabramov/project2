# project2

docker build -t nginx ./.nginx/
docker run -dit --name nginx -p 8081:80 nginx  
docker exec -it nginx bash
docker stop nginx && docker rm nginx && docker rmi nginx
