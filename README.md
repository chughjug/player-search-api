# Player Search API

A GitHub Actions workflow and Express API for searching US Chess players and exporting results as CSV files.

## Features

- 🔍 Search for US Chess players by name
- 📊 Export search results to CSV format
- ☁️ GitHub Actions workflow for automated searches
- 🚀 RESTful API endpoints
- 💾 Automatic CSV file storage

## Getting Started

### Installation

```bash
npm install
```

### Run the API Server

```bash
npm start
```

The server will start on `http://localhost:3000`

### Test the Search Functionality

```bash
npm test
```

Or search for a specific player:

```bash
node api/search-and-export.js "Player Name"
```

## API Endpoints

### Search Players (JSON)
```
GET /api/search?name=<player_name>&max=<number>
```

### Export Players as CSV
```
GET /api/export?name=<player_name>&max=<number>
```

### Search and Save to File
```
POST /api/search-and-save
Body: { "name": "Player Name", "max": 50 }
```

### List CSV Files
```
GET /api/files
```

### Get Specific CSV File
```
GET /api/file/:filename
```

### Health Check
```
GET /health
```

## GitHub Actions

The workflow can be triggered:

1. **Manually**: Go to Actions > Player Search API > Run workflow
2. **On push**: Automatically runs when code is pushed to main
3. **On schedule**: Runs every hour

### Usage

1. Navigate to the "Actions" tab in your GitHub repository
2. Select "Player Search API"
3. Click "Run workflow"
4. Enter a player name
5. The workflow will:
   - Search for players
   - Generate a CSV file
   - Upload results as artifacts
   - Publish to GitHub Pages (if enabled)

## Example Usage

### Command Line
```bash
node api/search-and-export.js Smith
```

### API Call
```bash
# Search for players (JSON)
curl "http://localhost:3000/api/search?name=Smith&max=10"

# Export as CSV
curl "http://localhost:3000/api/export?name=Smith&max=50" > results.csv

# Save and return file info
curl -X POST http://localhost:3000/api/search-and-save \
  -H "Content-Type: application/json" \
  -d '{"name": "Smith", "max": 20}'
```

### Direct File Access
```bash
# Download a specific CSV file
curl http://localhost:3000/data/results_Smith.csv
```

## CSV Format

The CSV export includes the following columns:

- `name` - Player's name
- `memberId` - USCF member ID
- `uscf_id` - USCF ID (alias)
- `state` - Player's state
- `rating_regular` - Regular rating
- `rating_quick` - Quick rating
- `rating_blitz` - Blitz rating
- `online_regular` - Online regular rating
- `online_quick` - Online quick rating
- `online_blitz` - Online blitz rating
- `expiration_date` - Membership expiration date

## Project Structure

```
.
├── .github/workflows/
│   └── player-search.yml    # GitHub Actions workflow
├── api/
│   ├── server.js            # Express API server
│   └── search-and-export.js # Search and CSV export logic
├── player_search.js         # Player search implementation
├── data/                    # Generated CSV files
├── package.json
└── README.md
```

## Dependencies

- **express** - Web server
- **axios** - HTTP client
- **cheerio** - HTML parsing
- **selenium-webdriver** - Browser automation
- **chromedriver** - Chrome driver for Selenium

## License

MIT

