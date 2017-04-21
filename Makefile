DOCKER_EXEC=docker-compose exec bellacia-api
COVERAGE=coverage run --source='./bellacia/'
TEST_DIR=tests/

test:
	$(DOCKER_EXEC) $(COVERAGE) manage.py test --failfast --setting=bellacia.core.settings.test -v2 $(TEST_DIR)
	$(DOCKER_EXEC) coverage report
