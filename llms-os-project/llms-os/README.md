# LLMs_OS Project

Enhanced workflow automation system with LLM integration.

## Build

```bash
docker build -t llms-os:v2 .
```

## Run

```bash
docker run --rm llms-os:v2 --help
docker run --rm llms-os:v2 example-workflow.yaml
```

## Structure

- `src/LLMs_OS/` - Main package
- `requirements.txt` - Dependencies
- `Dockerfile` - Container build
