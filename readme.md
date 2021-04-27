# Datadog Dogstatsd Example
An example running datadog agent in a container and using a simple 
python application to report dogstatsd metric to it.  

## Usage

Add your datadog api key to the environment or a dotenv file.

```
export DD_API_KEY=your key here
```

Bring docker-compose up:

```
docker-compose up
```

And install dependencies with poetry.

```
poetry run report
```
