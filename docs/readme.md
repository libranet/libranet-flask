# Libranet Demo Flask

## Introduction

Demo-package with a flask-project using the factory-pattern,
serving via gunicorn and managed by supervisord.



## Installation


```
cd <your-projects-dir>
git clone https://github.com/libranet/libranet-demo-flask
make install
```


## Running Flask
Start flask-developmenet-server in foreground:

```
make flask-run
```


Start gunicorn-server in foreground:

```
make gunicorn-run
```




## Running pytest
Run the unittests with pytest:

```
make pytest
```
