# INSTALL
install-dependencies:
	food-roulett-env/bin/pip install -r requirements.txt

# RUN
run-server:
	food-roulett-env/bin/python src/manage.py runserver

# UPDATE
update-dependencies:
	food-roulett-env/bin/pip freeze > requirements.txt
