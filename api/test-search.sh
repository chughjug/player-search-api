#!/bin/bash

# Test script for Player Search API
# Make sure the server is running: npm start

BASE_URL="${1:-http://localhost:3000}"
PLAYER_NAME="${2:-Smith}"

echo "Testing Player Search API at $BASE_URL"
echo "======================================"

echo -e "\n1. Health Check:"
curl -s "$BASE_URL/health" | jq '.'

echo -e "\n2. Search for players (JSON):"
curl -s "$BASE_URL/api/search?name=$PLAYER_NAME&max=5" | jq '.'

echo -e "\n3. Export as CSV:"
curl -s "$BASE_URL/api/export?name=$PLAYER_NAME&max=10" | head -20

echo -e "\n4. List available CSV files:"
curl -s "$BASE_URL/api/files" | jq '.'

echo -e "\n5. Save and return file info:"
curl -s -X POST "$BASE_URL/api/search-and-save" \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"$PLAYER_NAME\", \"max\": 20}" | jq '.'

echo -e "\n\nDone!"

