# AnunnakiWorld Website

A futuristic, ancient-alien themed website for the AnunnakiWorld trading system whitepaper.

## Quick Portainer Deployment with Cloudflare Tunnel

1. In Portainer:
   - Go to "Stacks" → "Add stack"
   - Select "Repository"
   - Fill in:
     ```
     Repository URL: https://github.com/skytechmk/anunnaki-web.git
     Repository reference: main
     Compose path: docker-compose.yml
     ```

2. Add Environment Variable:
   - Click "Add environment variable"
   - Add the following:
     ```
     TUNNEL_TOKEN=eyJhIjoiNDEyNTU1MTAwM2MyODk1ODI5Nzg0OGQ3MTNkMmQ3YjciLCJ0IjoiZWI0MDFhYzYtOTNjMy00OTdlLWIxYmMtZjEzODc5MzYyZjU0IiwicyI6IlpXSmhOV1ppTWpNdE5qTm1OQzAwTWpFNUxXSmtOalF0WXpsbFlUZzJPR0kxTkRVeiJ9
     ```

3. Click "Deploy the stack"

## Stack Components

```yaml
version: '3.8'

services:
  web:
    image: skytechmk/anunnaki-web:latest
    ports:
      - "24601:5000"
    environment:
      - FLASK_APP=app.py
      - FLASK_ENV=production
      - PYTHONUNBUFFERED=1
    restart: unless-stopped
    networks:
      - anunnaki-net

  cloudflared:
    image: cloudflare/cloudflared:latest
    command: tunnel run
    environment:
      - TUNNEL_TOKEN=${TUNNEL_TOKEN}
    restart: unless-stopped
    networks:
      - anunnaki-net
    depends_on:
      - web
```

## Monitoring

### View Tunnel Status
- In Portainer:
  1. Go to your stack
  2. Click on the cloudflared container
  3. Select "Logs" tab

### Check Web Service
- In Portainer:
  1. Go to your stack
  2. Click on the web container
  3. Select "Logs" tab

## Troubleshooting

If the tunnel isn't connecting:
1. Check cloudflared container logs
2. Verify the TUNNEL_TOKEN is correctly set
3. Ensure both containers are running

## Repository Structure

```
anunnaki-web/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── docker-compose.yml # Stack configuration with Cloudflare Tunnel
├── static/           # Static assets
└── templates/        # HTML templates
```

## Contact

- GitHub: @skytechmk
- Telegram: @Annunaki_World

## Security Notes

- The tunnel token is configured through Portainer environment variables
- Stack automatically handles secure tunnel connection
- All traffic is encrypted through Cloudflare's network
