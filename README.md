# Flask implementation of test task

## Instalation

```
$ python3 -m venv venv
$ . ./venv/bin/activate
$ make reqs
$ make db
$ make run (it starts dev server on localhost:8000)
```

## Endpoints

`GET /api/footballers` -- list of footballers

`POST /api/footballers` -- footballer creating endpoint

`DELETE /api/footballers/<int:id>/delete` -- footballer deleting endpoint
