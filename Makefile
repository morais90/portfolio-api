DOCKER_EXEC=docker-compose exec portfolio-api
COVERAGE=coverage run --source='./portfolio/'
TEST_DIR=tests

install:
	pip3 install -r requirements.txt

test:
	$(COVERAGE) manage.py test --failfast --setting=portfolio.core.settings.test -v2 $(TEST_DIR)
	coverage report

container-test:
	$(DOCKER_EXEC) $(COVERAGE) manage.py test --failfast --setting=portfolio.core.settings.test -v2 $(TEST_DIR)
	$(DOCKER_EXEC) coverage report
