# Libranet Flask

## Introduction

Demo-package with a flask-project using the factory-pattern,
serving via gunicorn and managed by supervisord.

## Installation

```
cd <your-projects-dir>
git clone https://github.com/libranet/libranet-flask
just install
```

## Running Flask

Start flask-development-server in foreground:

```
just flask-run
```

Start gunicorn-server in foreground:

```
just gunicorn-run
```

## Running pytest

Run the unittests with pytest:

```
just pytest
```
