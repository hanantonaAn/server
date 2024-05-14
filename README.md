docker stop server-app-1
docker rm server-app-1
docker-compose build 
docker-compose up

```
#RUN SERVER with uvicorn for ws protocol
python -m uvicorn server.asgi:application --reload 
```