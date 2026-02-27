# flask


# Define variables outside the recipe
# NEW_KEY=`echo $(RANDOM) | md5sum | head -c 20; echo`

# ## replace placeholder __SECRET_KEY__ with random value
# dotenv-set-flask-secret-key:
# 	echo -e "Replacing string __SECRET_KEY__ with random generated value" ;\
# 	$(SED) -i 's@__SECRET_KEY__@'"$(NEW_KEY)"'@' .env


# execute bin/flask run
flask-run:
	bin/flask run


# execute bin/gunicorn
flask-run-gunicorn:
	bin/gunicorn libranet_flask.main:create_app()


## execute bin/flask shell
flask-shell:
	bin/flask shell


# execute bin/uvicorn shell
flask-run-uvicorn:
	bin/uvicorn --factory libranet_flask.main:create_app
