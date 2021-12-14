# project2

# nginx
docker build -t nginx ./.nginx/
docker run -dit --name nginx -p 8081:80 nginx  
docker exec -it nginx bash
docker stop nginx && docker rm nginx && docker rmi nginx

# app
docker build -t app ./.app/  
docker run -dit --name app-1 -p 8082:80 app  
docker run -dit --name app-2 -p 8083:80 app  
docker exec -it app-1 bash
docker stop app-1 && docker rm app-1 && docker stop app-2 && docker rm app-2 && docker rmi app  
