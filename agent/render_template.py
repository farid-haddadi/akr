from jinja2 import Environment, FileSystemLoader # type: ignore

# Créer un environnement Jinja2
env = Environment(loader=FileSystemLoader('./structures'))

# Charger le template
template = env.get_template('test_1.jinja2')

# Exemple d'entrée utilisateur
user_input = input()
role = input()

# Rendre le template avec l'entrée utilisateur
request_body = template.render(user_input=user_input, role=role)

# Afficher le corps de la requête
print(request_body)