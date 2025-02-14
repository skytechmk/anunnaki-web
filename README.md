# AnunnakiWorld Website

A futuristic, ancient-alien themed website for the AnunnakiWorld trading system whitepaper.

## Cloudflare Tunnel Deployment

### 1. Set Up Cloudflare Tunnel

1. Install cloudflared CLI:
```bash
# On Debian/Ubuntu
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared.deb
```

2. Log in to Cloudflare:
```bash
cloudflared tunnel login
```

3. Create a tunnel:
```bash
cloudflared tunnel create anunnaki-web
```

4. Get your tunnel token:
```bash
cloudflared tunnel token <TUNNEL_ID>
```

5. Create a `.env` file:
```bash
echo "TUNNEL_TOKEN=your-tunnel-token-here" > .env
```

### 2. Deploy with Portainer

1. In Portainer:
   - Go to "Stacks" → "Add stack"
   - Select "Repository"
   - Fill in:
     ```
     Repository URL: https://github.com/skytechmk/anunnaki-web.git
     Repository reference: main
     Compose path: docker-compose.yml
     ```
   - Add Environment variables:
     - Click "Load variables from .env file"
     - Or manually add: `TUNNEL_TOKEN=your-tunnel-token-here`

2. Configure DNS:
```bash
cloudflared tunnel route dns <TUNNEL_ID> your-domain.com
```

### Docker Compose Configuration

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
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
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

networks:
  anunnaki-net:
    driver: bridge
```

### Monitoring Tunnel Status

1. View Tunnel Status:
```bash
cloudflared tunnel info <TUNNEL_NAME>
```

2. Check Logs in Portainer:
   - Go to your stack
   - Click on the cloudflared container
   - Select "Logs" tab

### Troubleshooting

1. Check Tunnel Connection:
```bash
cloudflared tunnel list
```

2. Verify DNS Configuration:
```bash
cloudflared tunnel route ip show
```

3. Common Issues:
   - If tunnel fails to connect, check:
     - TUNNEL_TOKEN is correct
     - DNS records are properly configured
     - Firewall settings allow outbound connections

## Alternative Deployment Methods

### Local Development
1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run locally:
```bash
python app.py
```

### Direct Docker Run
```bash
docker pull skytechmk/anunnaki-web:latest
docker run -p 24601:5000 skytechmk/anunnaki-web:latest
```

## Repository Structure

```
anunnaki-web/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── docker-compose.yml # Stack configuration with Cloudflare Tunnel
├── .env              # Environment variables (git-ignored)
├── static/           # Static assets
└── templates/        # HTML templates
```

## Contact

- GitHub: @skytechmk
- Telegram: @Annunaki_World

## Security Notes

- Keep your TUNNEL_TOKEN secure
- Don't commit .env file to git
- Regularly update cloudflared image
- Monitor tunnel access logs
