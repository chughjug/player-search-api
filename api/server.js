const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const { searchUSChessPlayers } = require('../player_search');
const { playersToCSV, saveCSV } = require('./search-and-export');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Serve static files from data directory
app.use('/data', express.static(path.join(__dirname, '../data')));

/**
 * Health check endpoint
 */
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

/**
 * Search endpoint - returns JSON
 */
app.get('/api/search', async (req, res) => {
  try {
    const playerName = req.query.name || req.query.player || 'Smith';
    const maxResults = parseInt(req.query.max || '10');

    console.log(`API search request for: ${playerName}`);

    const players = await searchUSChessPlayers(playerName, maxResults);

    res.json({
      query: playerName,
      count: players.length,
      players: players
    });
  } catch (error) {
    console.error('Search error:', error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * Export endpoint - returns CSV
 */
app.get('/api/export', async (req, res) => {
  try {
    const playerName = req.query.name || req.query.player || 'Smith';
    const maxResults = parseInt(req.query.max || '50');

    console.log(`Export request for: ${playerName}`);

    const players = await searchUSChessPlayers(playerName, maxResults);
    const csvContent = playersToCSV(players);

    res.setHeader('Content-Type', 'text/csv');
    res.setHeader('Content-Disposition', `attachment; filename=players_${playerName.replace(/[^a-zA-Z0-9]/g, '_')}.csv`);
    res.send(csvContent);
  } catch (error) {
    console.error('Export error:', error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * Search and save endpoint - saves CSV and returns file info
 */
app.post('/api/search-and-save', async (req, res) => {
  try {
    const playerName = req.body.name || req.body.player || 'Smith';
    const maxResults = parseInt(req.body.max || '50');

    console.log(`Search and save request for: ${playerName}`);

    const players = await searchUSChessPlayers(playerName, maxResults);
    const csvContent = playersToCSV(players);
    const filepath = saveCSV(csvContent, playerName);

    res.json({
      query: playerName,
      count: players.length,
      filepath: `/data/${path.basename(filepath)}`,
      players: players
    });
  } catch (error) {
    console.error('Search and save error:', error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * List available CSV files
 */
app.get('/api/files', (req, res) => {
  try {
    const dataDir = path.join(__dirname, '../data');
    
    if (!fs.existsSync(dataDir)) {
      return res.json({ files: [] });
    }

    const files = fs.readdirSync(dataDir)
      .filter(file => file.endsWith('.csv'))
      .map(file => ({
        name: file,
        url: `/data/${file}`,
        size: fs.statSync(path.join(dataDir, file)).size
      }));

    res.json({ files });
  } catch (error) {
    console.error('Files listing error:', error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * Get CSV file content
 */
app.get('/api/file/:filename', (req, res) => {
  try {
    const filename = req.params.filename;
    const filepath = path.join(__dirname, '../data', filename);

    if (!fs.existsSync(filepath)) {
      return res.status(404).json({ error: 'File not found' });
    }

    const csvContent = fs.readFileSync(filepath, 'utf8');
    
    res.setHeader('Content-Type', 'text/csv');
    res.setHeader('Content-Disposition', `attachment; filename=${filename}`);
    res.send(csvContent);
  } catch (error) {
    console.error('File read error:', error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * Root endpoint with API documentation
 */
app.get('/', (req, res) => {
  res.json({
    name: 'Player Search API',
    version: '1.0.0',
    endpoints: {
      'GET /health': 'Health check',
      'GET /api/search?name=<player_name>&max=<number>': 'Search for players (returns JSON)',
      'GET /api/export?name=<player_name>&max=<number>': 'Export players as CSV',
      'POST /api/search-and-save': 'Search and save CSV to disk (body: {name, max})',
      'GET /api/files': 'List available CSV files',
      'GET /api/file/:filename': 'Download specific CSV file',
      'GET /data/:filename': 'Serve CSV file directly'
    },
    example: {
      search: 'GET /api/search?name=Smith&max=10',
      export: 'GET /api/export?name=Smith&max=50',
      files: 'GET /api/files'
    }
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Player Search API server running on http://localhost:${PORT}`);
});

module.exports = app;

