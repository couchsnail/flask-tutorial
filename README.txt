Docker commands:
docker build -t user/container:tag
docker run user/container:tag

When running Flask, use command docker run -p port:port flask/app/name

If having problems pushing to Flask:
Login to docker.io
Make sure file is named user/container:tag
Then docker push user/container:tag
