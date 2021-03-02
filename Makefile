env:
	sudo rm -rf ./venv
	python3.8 -m venv venv
	./venv/bin/pip install -r requirements.txt

build:
	sudo docker-compose down
	cp ../requirements.txt .
	sudo docker-compose build

upd:
	sudo docker-compose up -d app

tail:
	sudo docker-compose logs app | tail -100
