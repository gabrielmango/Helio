
.PHONY: run i f t  c git

# Run the projet
run:
	@poetry shell
	
# Install dev dependences
i:
	@poetry add --group dev pytest isort mkdocs blue pylint python-dotenv
	@pylint --generate-rcfile > .pylintrc
	@mkdocs new .

# Format the code
f:
	@isort .
	@blue .
	@pylint helio

# Teste the code 
t:
	@pytest .

# Preper project to commit
c:
	@isort .
	@blue .

git:
	@git chechout main
	@git pull