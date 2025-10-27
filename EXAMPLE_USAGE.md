# Python API Client Examples

## Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or using pip3:

```bash
pip3 install -r requirements.txt
```

## Usage

### Simple Version (simple_client.py)

```bash
# Search for "Smith" (default)
python simple_client.py

# Search for a specific player
python simple_client.py Chugh

# Search with more results
python simple_client.py Kasparov 20
```

### Full-Featured Version (api_client.py)

```bash
# Search for "Smith" (default, 10 results)
python api_client.py

# Search for a specific player
python api_client.py Chugh

# Search with custom max results
python api_client.py Fischer 15
```

## Code Examples

### Basic API Call

```python
import requests

# Call the API
response = requests.get("http://localhost:3000/api/export", 
                       params={"name": "Smith", "max": 10})

# Get CSV data
csv_data = response.text
print(csv_data)
```

### Get JSON Response Instead of CSV

```python
import requests

# Call the search API (returns JSON)
response = requests.get("http://localhost:3000/api/search",
                       params={"name": "Smith", "max": 10})

# Parse JSON
data = response.json()
players = data['players']

for player in players:
    print(f"{player['name']} - Rating: {player['rating']}")
```

### Save CSV to File

```python
import requests

# Get CSV data
response = requests.get("http://localhost:3000/api/export",
                       params={"name": "Smith", "max": 50})

# Save to file
with open('players.csv', 'w') as f:
    f.write(response.text)

print("CSV saved to players.csv")
```

## API Endpoints

All examples use these API endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/search?name=X&max=10` | Search players (JSON) |
| GET | `/api/export?name=X&max=10` | Export CSV |
| GET | `/health` | Health check |

## Testing with Local Server

1. Start the server:
   ```bash
   npm start
   ```

2. Run the Python client:
   ```bash
   python simple_client.py Smith
   ```

## Production Usage

To use with a deployed API, change the `api_url` in the Python scripts:

```python
# For local development
api_url = "http://localhost:3000"

# For production (example)
api_url = "https://your-api-server.com"
```

## Error Handling

The scripts include basic error handling:

```python
try:
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    csv_data = response.text
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

