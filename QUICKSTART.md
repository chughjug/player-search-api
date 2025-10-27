# Quick Start - Player Search API

## 🚀 Get Started in 3 Steps

### Step 1: Install
```bash
npm install
```

### Step 2: Run
```bash
npm start
```

### Step 3: Use
```bash
# Search API
curl "http://localhost:3000/api/search?name=Smith"

# Export CSV
curl "http://localhost:3000/api/export?name=Smith" > results.csv
```

## 📋 Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/search?name=X&max=10` | Search players (JSON) |
| GET | `/api/export?name=X&max=10` | Export CSV |
| POST | `/api/search-and-save` | Search & save CSV |
| GET | `/api/files` | List CSV files |
| GET | `/api/file/:filename` | Get CSV file |

## 🔧 Command Line Usage

```bash
# Search from terminal
node api/search-and-export.js "Player Name"

# Search with default (Smith)
npm test
```

## ☁️ GitHub Actions

1. Push code to GitHub
2. Go to Actions tab
3. Run "Player Search API" workflow
4. Download results from artifacts

Or trigger via API call:
```bash
gh workflow run player-search.yml -f player_name=Smith
```

## 📊 CSV Format

The exported CSV includes:
- Player name, member ID, state
- Regular, Quick, Blitz ratings
- Online ratings
- Expiration date

## 📁 Project Structure

```
├── api/
│   ├── server.js              # Express API
│   ├── search-and-export.js   # Search logic
│   └── test-search.sh         # Test script
├── .github/workflows/
│   ├── player-search.yml       # Main workflow
│   └── deploy-api.yml         # Deployment workflow
├── player_search.js           # Search implementation
├── package.json
├── README.md                   # Full documentation
└── USAGE.md                    # Detailed usage
```

## 💡 Examples

### Example 1: Simple Search
```bash
curl "http://localhost:3000/api/search?name=Kasparov&max=5"
```

### Example 2: Export and Save
```bash
curl -X POST http://localhost:3000/api/search-and-save \
  -H "Content-Type: application/json" \
  -d '{"name": "Fischer", "max": 20}'
```

### Example 3: Download CSV
```bash
curl http://localhost:3000/data/results_Smith.csv -o my_results.csv
```

## 🎯 Common Tasks

**Search for a player:**
```bash
node api/search-and-export.js "Your Player Name"
```

**Start API server:**
```bash
npm start
```

**Test the API:**
```bash
./api/test-search.sh
```

**Check health:**
```bash
curl http://localhost:3000/health
```

## 📝 Need More Help?

- Read `README.md` for full documentation
- Read `USAGE.md` for detailed usage examples
- Check API documentation at `http://localhost:3000/`

