# Player Search - Usage Guide

## Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Run the API Server
```bash
npm start
```

The server will start on `http://localhost:3000`

## Usage Examples

### Command Line Search

Search for a player and generate CSV:
```bash
node api/search-and-export.js Smith
```

This will:
- Search for players with name "Smith"
- Generate a CSV file in the `data/` directory
- Display results in the console

### API Usage

#### 1. Health Check
```bash
curl http://localhost:3000/health
```

Response:
```json
{
  "status": "ok",
  "timestamp": "2024-01-15T10:30:00.000Z"
}
```

#### 2. Search Players (JSON Response)
```bash
curl "http://localhost:3000/api/search?name=Smith&max=10"
```

Response:
```json
{
  "query": "Smith",
  "count": 10,
  "players": [
    {
      "name": "John Smith",
      "memberId": "12345678",
      "uscf_id": "12345678",
      "state": "CA",
      "rating": 1800,
      "ratings": {
        "regular": 1800,
        "quick": 1750,
        "blitz": 1700
      }
    }
  ]
}
```

#### 3. Export as CSV (Download)
```bash
curl "http://localhost:3000/api/export?name=Smith&max=50" > results.csv
```

#### 4. Search and Save to Server
```bash
curl -X POST http://localhost:3000/api/search-and-save \
  -H "Content-Type: application/json" \
  -d '{"name": "Smith", "max": 20}'
```

Response:
```json
{
  "query": "Smith",
  "count": 20,
  "filepath": "/data/results_Smith.csv",
  "players": [...]
}
```

#### 5. List Available CSV Files
```bash
curl http://localhost:3000/api/files
```

Response:
```json
{
  "files": [
    {
      "name": "results_Smith.csv",
      "url": "/data/results_Smith.csv",
      "size": 2458
    }
  ]
}
```

#### 6. Download Specific CSV File
```bash
curl http://localhost:3000/data/results_Smith.csv
```

## GitHub Actions Usage

### Manual Trigger

1. Go to your GitHub repository
2. Navigate to **Actions** tab
3. Select **Player Search API** workflow
4. Click **Run workflow**
5. Enter a player name
6. Click **Run workflow**

### Automatic Schedule

The workflow runs automatically every hour on the schedule defined in the workflow.

### View Results

After the workflow completes:
1. Go to the **Actions** tab
2. Click on the completed workflow run
3. Scroll to **Artifacts** section
4. Download the `player-results` artifact
5. Extract the CSV files

## Advanced Usage

### Using the Test Script

```bash
# Test with default player name (Smith)
./api/test-search.sh

# Test with custom player name
./api/test-search.sh http://localhost:3000 "Jones"

# Test against different server
./api/test-search.sh https://api.example.com "Smith"
```

### Programmatic Usage

```javascript
const { searchUSChessPlayers } = require('./player_search');
const { playersToCSV } = require('./api/search-and-export');

async function searchAndExport() {
  const players = await searchUSChessPlayers('Smith', 10);
  const csv = playersToCSV(players);
  console.log(csv);
}

searchAndExport();
```

### Batch Processing

```bash
# Search for multiple players
for player in Smith Jones Williams; do
  node api/search-and-export.js "$player"
done
```

## Configuration

### Environment Variables

```bash
# Set port
PORT=8080 npm start

# Set max results
export MAX_RESULTS=100
```

### API Configuration

Edit `api/server.js` to customize:
- Default port
- Rate limiting
- CORS settings
- File storage location

## Troubleshooting

### Server won't start
- Ensure Node.js 18+ is installed
- Check if port 3000 is available
- Install dependencies: `npm install`

### No results found
- Check player name spelling
- Try partial names
- Increase timeout in search functions

### CSV file issues
- Check `data/` directory exists
- Ensure write permissions
- Check disk space

## API Response Time

- **Sub-second search**: Best for frequently searched players (cached results)
- **Ultra-fast search**: Good for new searches (200-500ms)
- **Fast search**: Standard performance (500ms-2s)
- **Original search**: Full Python integration (2-5s)

