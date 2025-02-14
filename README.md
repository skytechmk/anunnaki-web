# AnunnakiWorld Website

A futuristic, ancient-alien themed website for the AnunnakiWorld trading system whitepaper.

## Portainer Deployment

1. In Portainer:
   - Go to "Stacks" → "Add stack"
   - Name your stack (e.g., "anunnaki-web")
   - Copy and paste this docker-compose configuration:

```yaml
version: '3.8'

services:
  web:
    image: skytechmk/anunnaki-web:latest
    ports:
      - "24601:5000"  # Host port 24601, container port 5000
    environment:
      - FLASK_APP=app.py
      - FLASK_ENV=production
      - PYTHONUNBUFFERED=1
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    restart: unless-stopped
    networks:
      - anunnaki-net

networks:
  anunnaki-net:
    driver: bridge
```

2. Click "Deploy the stack"
3. Access the website at `http://your-server-ip:24601`

### Monitoring in Portainer

1. View Logs:
   - Go to your stack
   - Click on the container
   - Select "Logs" tab
   - You'll see logs similar to:
   ```
   * Serving Flask app 'app'
   * Running on http://127.0.0.1:5000
   * Running on http://172.17.0.5:5000
   ```

2. Monitor Resources:
   - Container stats available in the "Stats" tab
   - Network information in the "Networks" tab

### Troubleshooting

If you see warnings like:
```
WARNING! This is a development server. Do not use it in a production deployment.
```
This is normal for Flask development server - it's safe for testing but consider using gunicorn for production.

## Alternative Deployment Methods

### Direct Docker Run
```bash
docker pull skytechmk/anunnaki-web:latest
docker run -p 24601:5000 skytechmk/anunnaki-web:latest
```

### Local Docker Compose
```bash
docker-compose up -d
```

## Development Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run locally:
```bash
python app.py
```

## Features

- Futuristic design with ancient alien theme
- Interactive glowing effects
- Responsive layout
- Pure CSS animations
- Containerized deployment
- Logging configuration
- Network isolation

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

## Contact

- GitHub: @skytechmk
- Telegram: @Annunaki_World
