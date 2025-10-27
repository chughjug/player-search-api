# Deploy to Heroku

## Quick Deploy (One Command)

```bash
heroku create player-search-api-app
git push heroku main
```

## Manual Deployment Steps

### 1. Prerequisites

- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Login to Heroku: `heroku login`

### 2. Create Heroku App

```bash
# Create a new Heroku app
heroku create player-search-api-app

# Or use an existing app
heroku apps:info
```

### 3. Set Buildpacks

```bash
# Add Node.js buildpack
heroku buildpacks:add heroku/nodejs

# Add Chrome buildpack for Selenium
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome

# Verify buildpacks
heroku buildpacks
```

### 4. Configure Environment Variables (Optional)

```bash
# Set Node environment
heroku config:set NODE_ENV=production

# View all config vars
heroku config
```

### 5. Deploy

```bash
# Initialize git if not already done
git init

# Add Heroku remote
heroku git:remote -a player-search-api-app

# Deploy
git push heroku main

# Or if using a different branch
git push heroku your-branch:main
```

### 6. Open the App

```bash
# Open in browser
heroku open

# View logs
heroku logs --tail
```

## Verifying Deployment

### Test the API

```bash
# Health check
curl https://player-search-api-app.herokuapp.com/health

# Search for players
curl "https://player-search-api-app.herokuapp.com/api/search?name=Smith&max=5"

# Export CSV
curl "https://player-search-api-app.herokuapp.com/api/export?name=Chugh" > results.csv
```

### Python Client Usage

```python
import requests

# Use your Heroku app URL
api_url = "https://player-search-api-app.herokuapp.com"

# Call the API
response = requests.get(f"{api_url}/api/export", 
                       params={"name": "Chugh", "max": 10})

# Get CSV data
csv_data = response.text
print(csv_data)
```

## Managing Your App

### View Logs

```bash
# Real-time logs
heroku logs --tail

# Last 100 lines
heroku logs -n 100
```

### Restart Dyno

```bash
heroku restart
```

### Scale Dyno

```bash
# Scale to 2 dynos
heroku ps:scale web=2
```

### Open Console

```bash
heroku run bash
```

### Update Application

```bash
# Make changes to your code
git add .
git commit -m "Update code"

# Deploy to Heroku
git push heroku main
```

## Troubleshooting

### Chrome/ChromeDriver Issues

If you encounter Chrome issues, add to your app:

```bash
heroku config:set GOOGLE_CHROME_SHIM=/app/.apt/usr/bin/google-chrome-stable
```

### Memory Issues

```bash
# View dyno info
heroku ps

# Scale up if needed
heroku ps:scale web=1:standard-1x
```

### Build Failures

```bash
# Check build logs
heroku logs --tail

# Clear build cache
heroku repo:purge_cache -a player-search-api-app
```

### Timeout Issues

The free Heroku dyno sleeps after 30 minutes of inactivity. Consider:

```bash
# Use a paid dyno to avoid sleeping
heroku ps:scale web=1:eco
```

Or set up [Kaffeine](https://kaffeine.herokuapp.com/) to keep your dyno awake.

## Configuration Files

### Procfile

```
web: node api/server.js
```

### app.json

```json
{
  "name": "Player Search API",
  "description": "US Chess player search API",
  "buildpacks": [
    {"url": "heroku/nodejs"},
    {"url": "https://github.com/heroku/heroku-buildpack-google-chrome"}
  ]
}
```

## Environment Variables

You can set custom environment variables:

```bash
# Example: Set API timeout
heroku config:set API_TIMEOUT=60000

# Example: Set max results limit
heroku config:set MAX_RESULTS=100
```

Access in your code:

```javascript
const timeout = process.env.API_TIMEOUT || 30000;
const maxResults = parseInt(process.env.MAX_RESULTS) || 50;
```

## Monitoring

### View Metrics

```bash
# Resource usage
heroku ps:exec

# Check dyno type
heroku ps:type
```

### Set Up Monitoring

Consider using [Heroku Metrics](https://devcenter.heroku.com/articles/metrics) or [New Relic](https://devcenter.heroku.com/articles/newrelic).

## Security

### Use HTTPS

Heroku automatically provides HTTPS for all apps.

### API Keys

Store sensitive keys as environment variables:

```bash
heroku config:set API_KEY=your_secret_key
```

Access in code:

```javascript
const apiKey = process.env.API_KEY;
```

## Cost Considerations

- **Free Tier**: 550-1000 hours/month (sleeps after inactivity)
- **Eco Dyno**: $5/month (always on)
- **Basic Dyno**: $7/month (always on, better performance)

## Next Steps

After deployment:

1. Test all API endpoints
2. Monitor logs for errors
3. Set up custom domain (optional)
4. Configure monitoring and alerts
5. Consider using a persistent database for caching

## Support

- [Heroku Docs](https://devcenter.heroku.com/)
- [Heroku Status](https://status.heroku.com/)
- [Heroku Support](https://help.heroku.com/)

