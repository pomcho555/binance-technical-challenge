# binance-technical-challenge
Technical Challenge

## Set up

```sh
poetry install
```

## Confirm submissions


### Only Q1~Q5
```sh
poetry run python run_answer.py
```

### Q6

## Run test
```sh
poetry run pytest \
  --cov=questions \
  --cov-branch \
  -v ./tests/* \
  --cov-report=html
```




## Run metrics server for Prometheus

```sh
docker-compose up
```

You can see the output accessible by querying [http://localhost:8080/metrics](http://localhost:8080/metrics). And you can access prometheus server: [http://localhost:9090/](http://localhost:9090/)


Shutdown all resources.

```sh
docker-compose down
```


### Docker Only

```sh
docker build -t test-questions .
```

```sh
docker run -p 8080:8080 --rm test-questions
```

You can see the output accessible by querying [http://localhost:8080/metrics](http://localhost:8080/metrics)

