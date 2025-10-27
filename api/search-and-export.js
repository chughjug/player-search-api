const fs = require('fs');
const path = require('path');
const { searchUSChessPlayers } = require('../player_search');

/**
 * Convert player data to CSV format
 */
function playersToCSV(players) {
  if (!players || players.length === 0) {
    return 'No players found';
  }

  // Define CSV headers
  const headers = [
    'name',
    'memberId',
    'uscf_id',
    'state',
    'rating_regular',
    'rating_quick',
    'rating_blitz',
    'online_regular',
    'online_quick',
    'online_blitz',
    'expiration_date'
  ];

  // Create CSV header row
  let csv = headers.join(',') + '\n';

  // Add each player as a row
  players.forEach(player => {
    const row = [
      `"${(player.name || '').replace(/"/g, '""')}"`,
      player.memberId || '',
      player.uscf_id || player.memberId || '',
      player.state || '',
      player.ratings?.regular || '',
      player.ratings?.quick || '',
      player.ratings?.blitz || '',
      player.ratings?.online_regular || '',
      player.ratings?.online_quick || '',
      player.ratings?.online_blitz || '',
      player.expiration_date || ''
    ];
    csv += row.join(',') + '\n';
  });

  return csv;
}

/**
 * Save CSV file and return its path
 */
function saveCSV(csvContent, searchTerm) {
  const dataDir = path.join(__dirname, '../data');
  
  // Create data directory if it doesn't exist
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
  }

  // Create filename from search term
  const filename = `results_${searchTerm.replace(/[^a-zA-Z0-9]/g, '_')}.csv`;
  const filepath = path.join(dataDir, filename);

  // Write CSV file
  fs.writeFileSync(filepath, csvContent, 'utf8');
  
  return filepath;
}

/**
 * Main function to search and export
 */
async function main() {
  const searchTerm = process.argv[2] || 'Smith';
  console.log(`Searching for players with name: ${searchTerm}`);

  try {
    // Perform search
    const players = await searchUSChessPlayers(searchTerm, 50);
    console.log(`Found ${players.length} players`);

    // Convert to CSV
    const csvContent = playersToCSV(players);
    console.log('\nCSV Content:');
    console.log(csvContent);

    // Save CSV file
    const filepath = saveCSV(csvContent, searchTerm);
    console.log(`\nCSV saved to: ${filepath}`);

    // Return file info as JSON
    const result = {
      searchTerm,
      playerCount: players.length,
      filepath,
      csvContent,
      players
    };

    console.log('\n=== Search Complete ===');
    console.log(JSON.stringify(result, null, 2));

    return result;
  } catch (error) {
    console.error('Error searching for players:', error);
    process.exit(1);
  }
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = {
  playersToCSV,
  saveCSV,
  main
};

