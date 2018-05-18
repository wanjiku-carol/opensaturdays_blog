
db:
	@ docker-compose up

db_silent:
	@ docker-compose up -d


clean:
	@ docker-compose down -v
