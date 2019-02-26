# INSTALL
install-dependencies:
	venv/bin/pip install -r requirements.txt

# RUN
run-server:
	venv/bin/python src/manage.py runserver

# UPDATE
update-dependencies:
	venv/bin/pip freeze > requirements.txt
