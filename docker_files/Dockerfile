#имя базового образа
FROM centos:latest
#создаем папку, где будет наша программа
RUN mkdir -p /go/src/app
#идем в папку
WORKDIR /go/src/app

#копируем все файлы из текущего пути к файлу Docker на вашей системе в нашу новую папку образа
COPY . /go/src/app