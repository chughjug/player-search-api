#!/usr/bin/env python3
"""
Player Search CLI - Search for US Chess players by name
Usage: python3 search_player.py "Player Name"
"""

import requests
import sys
import os

# Heroku API URL
API_URL = "https://player-search-api-60b22a3031bd.herokuapp.com"


def search_players(name, max_results=10):
    """Search for players using the API"""
    try:
        url = f"{API_URL}/api/search"
        params = {
            "name": name,
            "max": max_results
        }
        
        print(f"\n🔍 Searching for: {name}...")
        response = requests.get(url, params=params, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        return data
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def print_table(players):
    """Print players in a formatted table"""
    if not players or len(players) == 0:
        print("\n   No players found.")
        return
    
    # Table header
    header = f"\n{'Name':<35} {'ID':<12} {'State':<6} {'Regular':<10} {'Quick':<10} {'Blitz':<10}"
    print("=" * 92)
    print(header)
    print("=" * 92)
    
    # Table rows
    for player in players:
        name = player.get('name', '').replace('\n', ' ').strip()
        member_id = player.get('memberId', '').strip()
        state = player.get('state') or 'N/A'
        if isinstance(state, str):
            state = state.strip()
        else:
            state = str(state)
        ratings = player.get('ratings', {})
        regular = ratings.get('regular', '') or ''
        quick = ratings.get('quick', '') or ''
        blitz = ratings.get('blitz', '') or ''
        
        # Truncate long names
        if len(name) > 34:
            name = name[:31] + '...'
        
        print(f"{name:<35} {member_id:<12} {state:<6} {regular:<10} {quick:<10} {blitz:<10}")
    
    print("=" * 92)
    print(f"\n✅ Found {len(players)} player(s)\n")


def main():
    """Main function"""
    # Get player name from command line
    if len(sys.argv) < 2:
        print("\n📋 Player Search CLI")
        print("Usage: python3 search_player.py \"Player Name\" [max_results]")
        print("\nExample:")
        print("  python3 search_player.py Smith")
        print("  python3 search_player.py \"Chugh\" 20")
        sys.exit(1)
    
    player_name = sys.argv[1]
    max_results = 10
    
    # Get max results if provided
    if len(sys.argv) > 2:
        try:
            max_results = int(sys.argv[2])
        except ValueError:
            print("⚠️  Invalid max_results, using default (10)")
    
    # Search for players
    data = search_players(player_name, max_results)
    
    if data and 'players' in data:
        print_table(data['players'])
        
        # Optionally print full details
        if len(sys.argv) > 2 and sys.argv[2] == '--verbose':
            print("\n📊 Full JSON Response:")
            print(f"{'='*92}")
            for i, player in enumerate(data['players'], 1):
                print(f"\n{i}. {player.get('name', 'Unknown').replace(chr(10), ' ')}")
                print(f"   ID: {player.get('memberId', 'N/A')}")
                print(f"   State: {player.get('state', 'N/A')}")
                print(f"   Ratings: {player.get('ratings', {})}")
                print(f"   Expiration: {player.get('expiration_date', 'N/A')}")
    else:
        print("\n❌ Failed to retrieve player data")


if __name__ == "__main__":
    main()

