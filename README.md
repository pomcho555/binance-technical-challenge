# binance-technical-challenge
Technical Challenge

## Set up

```sh
poetry install
```

## Run test
```sh
poetry run pytest \
  --cov=questions \
  --cov-branch \
  -v ./tests/* \
  --cov-report=html
```