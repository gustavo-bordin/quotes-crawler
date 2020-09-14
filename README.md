# Random quotes generator's database filler
https://github.com/gustavobordinho/random-quotes-generator

### 1. Used tools

- `scrapy ` - 2.3.0
- `pymongo ` - 3.11.0
- `python-dotenv` - 0.14.0
- `docker` - 19.03.12
- `docker-compose` - 1.26.2
<br>
<br>
<hr>
<br>

### 2. Setting up

<br>

#### 2.1. Download and install `docker` at: https://www.docker.com/products/docker-desktop

<br>

`P.S: If you are using windows or MacOs, you docker-compose already comes with the default installation. Only follow the step 2.2 if you use linux.`

#### 2.2. Download and install `docker compose` at: https://docs.docker.com/compose/install/

<br>

#### 2.3. Create your credentials file (`.env`):

```bash
$ mv .env.example .env
```

#### 2.4. Edit the created `.env` file with your own credentials

<br>

#### 2.4. Create the docker images:

```bash
$ docker-compose build; docker-compose up -d
```

#### 2.5. Once it is created and running, execute the script to fill your database:

```
$ docker-compose exec app scrapy runspider quotes.py
```
