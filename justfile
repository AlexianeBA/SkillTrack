# Start the microservices
docker-up:
    docker-compose up --build

# Stop the microservices
docker-down:
    docker-compose down --remove-orphans

#clean docker
docker-clean-projet:
    docker-compose down --remove-orphans
    docker system prune -a

docker-build-backend:
    cd backend && docker build -t backend . && cd ..

docker-build-frontend:
    cd frontend && docker build -t frontend . && cd ..

docker-rm container_id:
    docker rm {{container_id}}

build-all:
    just docker-clean-projet
    just docker-build-backend
    # just docker-build-generation-service
build-and-run:
    just build-all
    just docker-up

runserver:
    cd backend && python manage.py runserver