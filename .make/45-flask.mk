# See ../makefile


# Define variables outside the recipe
NEW_KEY=`echo $(RANDOM) | md5sum | head -c 20; echo`
.PHONY: dotenv-set-flask-secret-key  ## replace placeholder __SECRET_KEY__ with random value
dotenv-set-flask-secret-key:
	echo -e "Replacing string __SECRET_KEY__ with random generated value" ;\
	$(SED) -i 's@__SECRET_KEY__@'"$(NEW_KEY)"'@' .env


.PHONY: flask-run  ## execute bin/flask run
flask-run:
	bin/flask run


.PHONY: flask-run-gunicorn  ## execute bin/gunicorn
flask-run-gunicorn:
	bin/gunicorn libranet_flask.main:create_app()


.PHONY: flask-shell  ## execute bin/flask shell
flask-shell:
	bin/flask shell


.PHONY: flask-run-uvicorn  ## execute bin/uvicorn shell
flask-run-uvicorn:
	bin/uvicorn --factory libranet_flask.main:create_app
