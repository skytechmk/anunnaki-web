# AnunnakiWorld Website

A futuristic, ancient-alien themed website for the AnunnakiWorld trading system whitepaper.

## Running with Docker (Recommended)

1. Make sure you have Docker and Docker Compose installed:
```bash
docker --version
docker-compose --version
```

2. Build and run the container:
```bash
# Build and start
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

3. Open in browser:
- Visit http://localhost:5000

4. Stop the container:
```bash
docker-compose down
```

## Manual Setup (Alternative)

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the website:
```bash
python app.py
```

3. Open in browser:
- Visit http://localhost:5000

## Features

- Futuristic design with ancient alien theme
- Interactive glowing effects
- Responsive layout
- Pure CSS animations
- No image dependencies
- Dockerized for easy deployment

## Structure

```
ANUN_WEB/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose configuration
├── static/
│   ├── whitepaper.css # Styles
│   └── whitepaper.js  # Interactive features
└── templates/
    └── whitepaper.html # Main page
```

## Contact

- GitHub: @skytechmk
- Telegram: @Annunaki_World

## Docker Commands Reference

```bash
# Build the image
docker build -t anunnaki-web .

# Run the container
docker run -p 5000:5000 anunnaki-web

# View running containers
docker ps

# Stop container
docker stop <container_id>

# Remove container
docker rm <container_id>

# Remove image
docker rmi anunnaki-web
