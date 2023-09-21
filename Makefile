migrate:
	@echo "Migrating database..."
	@python manage.py migrate

makemigrations:
	@echo "Making migrations..."
	@python manage.py makemigrations

run:
	@echo "Running server..."
	@python manage.py runserver

shell:
	@echo "Running shell..."
	@python manage.py shell

createsuperuser:
	@echo "Creating superuser..."
	@python manage.py createsuperuser

startapp:
	@echo "Creating app..."
	@cd apps && django-admin startapp $(APP_NAME) && cd ..

dropdb-psql:
	@echo "Checking if database exists..."
	@sudo psql -U postgres -d postgres -c "SELECT datname FROM pg_database WHERE datname = '$(DB_NAME)';" | grep -q $(DB_NAME) || (echo "Database does not exist" && exit 1)
	@echo "Deleting database..."
	@sudo psql -U postgres -c "DROP DATABASE $(DB_NAME);"
