# ProjetosDevOps da Faculdade Impacta

## Integrantes

| Nome | RA | Linkedin | Github |
|:---:|:---:|:---:|:---:|
| Vinícius Bittencourt | 2201032 | [vini linkedin](https://www.linkedin.com/in/vin%C3%ADcius-bittencourt-b98386236/) | [vini git](github.com/vinisbitten) |
|Carlos Albuquerque | 2200823 | [carlos linkedin](https://www.linkedin.com/in/carlos-albuquerque-639611162/) | [carlos git](https://github.com/CarlosAlbuquerque) |
| Guilherme Aragão | N/A | ? | ? |

## Projetos

### API Pokedex Dockerized

- Using local docker registry

```bash
# clone the repo
git clone https://gitlab.com/vinicius-bittencourt-impacta/my-devops-project.git

# go to the project folder
cd my-devops-project

# build the image
docker build -t pokedex-api .

# run the container
docker run -p 8080:8080 pokedex-api
```

- Using docker hub

```bash
# run the image
docker run -p 8080:8080 vinisbitten/pokedex-api
```

- Search for a pokémon
```http://localhost:8080/pokemon/{pokename}```
