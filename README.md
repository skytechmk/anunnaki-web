# AnunnakiWorld Website

A futuristic, ancient-alien themed website for the AnunnakiWorld trading system whitepaper.

## Deploy via Portainer Stack (Recommended)

### Method 1: Direct from GitHub Repository

1. In Portainer:
   - Go to "Stacks" → "Add stack"
   - Select "Repository" as build method
   - Fill in the following:
     ```
     Repository URL: https://github.com/skytechmk/anunnaki-web.git
     Repository reference: main
     Compose path: docker-compose.yml
     ```
   - Click "Deploy the stack"

### Method 2: Manual Configuration

If you prefer to configure manually:
1. In Portainer:
   - Go to "Stacks" → "Add stack"
   - Select "Web editor"
   - Copy and paste this configuration:

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
3. Access at `http://your-server-ip:24601`

## Stack Auto-Updates

To enable automatic updates when the repository changes:
1. In Portainer stack settings:
   - Enable "Automatic Updates"
   - Set "Update Interval" (e.g., 5 minutes)
   - Select "Always pull image"

## Monitoring

### View Logs
- Go to your stack
- Click on the container
- Select "Logs" tab
- Example logs:
  ```
  * Serving Flask app 'app'
  * Running on http://127.0.0.1:5000
  * Running on http://172.17.0.5:5000
  ```

### Monitor Resources
- Container stats in "Stats" tab
- Network info in "Networks" tab

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

## Development

### Local Setup
1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run locally:
```bash
python app.py
```

## Repository Structure

```
anunnaki-web/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── docker-compose.yml # Stack configuration
├── static/           # Static assets
└── templates/        # HTML templates
```

## Contact

- GitHub: @skytechmk
- Telegram: @Annunaki_World

## Stack Configuration Details

### Environment Variables
- `FLASK_APP`: Main application file
- `FLASK_ENV`: Production/Development mode
- `PYTHONUNBUFFERED`: Ensures immediate log output

### Logging Configuration
- Driver: json-file
- Max size: 10MB
- Max files: 3

### Network Configuration
- Custom bridge network: anunnaki-net
- Isolated container networking
