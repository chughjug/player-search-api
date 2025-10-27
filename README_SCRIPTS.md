# Player Search Scripts - Run From Anywhere!

## Quick Start

### Option 1: Full Featured (requires `requests`)
```bash
python3 search_player.py "Player Name" [max_results]
```

### Option 2: Standalone (no dependencies)
```bash
python3 search "Player Name" [max_results]
```

## Examples

```bash
# Search for Smith (default 10 results)
python3 search_player.py Smith

# Search for Chugh with 20 results
python3 search_player.py Chugh 20

# Search using standalone version
python3 search "Fischer" 5
```

## Make It Global (Run from Anywhere)

### 1. Copy Script to Your Path

#### On macOS/Linux:
```bash
# Copy to a directory in your PATH
sudo cp search_player.py /usr/local/bin/psearch
sudo chmod +x /usr/local/bin/psearch

# Or copy to your ~/bin directory (create it first)
mkdir -p ~/bin
cp search_player.py ~/bin/psearch
chmod +x ~/bin/psearch
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

#### Or Use Aliases:
```bash
# Add to your ~/.zshrc or ~/.bashrc
alias psearch='python3 /path/to/search_player.py'
alias psearch-simple='python3 /path/to/search'
```

### 2. Then Run From Anywhere:
```bash
psearch Smith
psearch "Chugh" 20
```

## Scripts Overview

### `search_player.py`
- Full-featured script
- Requires: `requests` library
- Better error handling
- More features (verbose mode, etc.)

### `search`
- Standalone script
- No dependencies - uses Python standard library only
- Works anywhere Python is installed
- Uses urllib instead of requests

## API Details

- **URL**: https://player-search-api-60b22a3031bd.herokuapp.com
- **Health**: `/health`
- **Search**: `/api/search?name=X&max=10`
- **Export CSV**: `/api/export?name=X&max=10`

## Output Format

```
============================================================================================

Name                                ID           State  Regular    Quick      Blitz     
============================================================================================
Aarush CHUGH                        14970943     NC     1568       1485       1319      
Aditya CHUGH                        15766057     IL     1160       951        1180      
============================================================================================

✅ Found 2 player(s)
```

## Troubleshooting

### Script not found
- Make sure the script is in your PATH
- Or use full path: `python3 /path/to/search_player.py Smith`

### Connection error
- Check if you're connected to the internet
- Verify API is running: `curl https://player-search-api-60b22a3031bd.herokuapp.com/health`

### Import error
For `search_player.py`, install requests:
```bash
pip3 install requests
# or
pip3 install --user requests
```

## Customization

Edit the `API_URL` at the top of the script to point to:
- Your own Heroku deployment
- Local server: `http://localhost:3000`
- Another API endpoint

```python
API_URL = "https://your-custom-api.com"
```

