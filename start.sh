docker build -t app ./.app/
docker-compose up -d

read -t 5 -p "Wait for 5 seconds..."
docker exec -it rabbit-2 rabbitmqctl stop_app
docker exec -it rabbit-2 rabbitmqctl join_cluster rabbit@rabbit-1
docker exec -it rabbit-2 rabbitmqctl start_app
