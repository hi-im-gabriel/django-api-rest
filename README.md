 <h1 align="center">RESTful Todolist API</h1>
   <p align="center">
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Django-green.svg" />
    </a>
    <a href="https://www.docker.com/">
    	<img src="https://img.shields.io/badge/built%20with-Docker-blue.svg" />
    </a>
  </p>
  
### GET ```todolist/```
  <p align="center">
  <img src="https://i.imgur.com/jUPMvcc.png"">
</p>

### POST ```todolist/```
> {"desc" : "Description of task to do"}

  <p align="center">
  <img src="https://i.imgur.com/GqVIZVf.png"">
</p>

### DELETE ```todolist/<int:id>```
  <p align="center">
  <img src="https://i.imgur.com/RWRguxq.png"">
</p>

### PUT ```todolist/<int:id>```
  <p align="center">
  <img src="https://i.imgur.com/fxwY2g2.png"">
</p>

# Requirements
  - Docker
  - docker-compose
  
# Running server

> Build service
```
docker-compose build
```

> Start/(re)create container
```
docker-compose up
```
or, if you want to run container in the background
```
docker-compose up -d
```

# Stopping server
```
docker-compose down
```