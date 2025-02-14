# AnunnakiWorld Website

A futuristic, ancient-alien themed website for the AnunnakiWorld trading system whitepaper.

## Quick Start with Docker

Pull and run the image directly from Docker Hub:
```bash
docker pull skytechmk/anunnaki-web:latest
docker run -p 5000:5000 skytechmk/anunnaki-web:latest
```

Or using Docker Compose:
```bash
docker-compose up
```

## Portainer Setup

To deploy using Portainer:

1. In Portainer, go to "Stacks" → "Add stack"
2. Copy and paste this docker-compose.yml content:
```yaml
version: '3.8'

services:
  web:
    image: skytechmk/anunnaki-web:latest
    ports:
      - "5000:5000"
    environment:
      - FLASK_APP=app.py
      - FLASK_ENV=production
    restart: unless-stopped
```
3. Click "Deploy the stack"

## Local Development Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the website:
```bash
python app.py
```

## Features

- Futuristic design with ancient alien theme
- Interactive glowing effects
- Responsive layout
- Pure CSS animations
- No image dependencies

## Structure

```
ANUN_WEB/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── docker-compose.yml # Docker Compose setup
├── static/
│   ├── whitepaper.css # Styles
│   └── whitepaper.js  # Interactive features
└── templates/
    └── whitepaper.html # Main page
```

## Docker Commands

```bash
# Pull the image
docker pull skytechmk/anunnaki-web:latest

# Run the container
docker run -p 5000:5000 skytechmk/anunnaki-web:latest

# Build locally
docker build -t skytechmk/anunnaki-web:latest .

# Push to Docker Hub (requires login)
docker push skytechmk/anunnaki-web:latest
```

## Contact

- GitHub: @skytechmk
- Telegram: @Annunaki_World
