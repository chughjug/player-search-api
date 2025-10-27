#!/usr/bin/env python3
"""
Player Search API Client
Calls the public API to search for players and retrieve CSV data
"""

import requests
import sys
import csv
from io import StringIO


def search_players(api_url, player_name, max_results=10):
    """
    Search for players using the API
    
    Args:
        api_url: Base URL of the API (e.g., "http://localhost:3000")
        player_name: Name to search for
        max_results: Maximum number of results to return
    
    Returns:
        dict: Response data with players
    """
    try:
        url = f"{api_url}/api/search"
        params = {
            "name": player_name,
            "max": max_results
        }
        
        print(f"🔍 Searching for: {player_name}...")
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        print(f"✅ Found {data.get('count', 0)} players\n")
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error calling API: {e}")
        return None


def export_csv(api_url, player_name, max_results=10):
    """
    Get CSV data directly from the API
    
    Args:
        api_url: Base URL of the API
        player_name: Name to search for
        max_results: Maximum number of results to return
    
    Returns:
        str: CSV content as string
    """
    try:
        url = f"{api_url}/api/export"
        params = {
            "name": player_name,
            "max": max_results
        }
        
        print(f"📥 Exporting CSV for: {player_name}...")
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        
        csv_data = response.text
        print(f"✅ CSV data retrieved ({len(csv_data)} bytes)\n")
        
        return csv_data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error retrieving CSV: {e}")
        return None


def print_csv_table(csv_data):
    """
    Print CSV data as a formatted table
    
    Args:
        csv_data: CSV content as string
    """
    if not csv_data:
        print("No CSV data to display")
        return
    
    # Parse CSV
    csv_file = StringIO(csv_data)
    reader = csv.DictReader(csv_file)
    
    # Print table header
    print("\n" + "=" * 120)
    print(f"{'Name':<35} {'Member ID':<12} {'State':<6} {'Regular':<10} {'Quick':<10} {'Blitz':<10}")
    print("=" * 120)
    
    # Print table rows
    for row in reader:
        name = row.get('name', '').replace('\n', ' ').strip()
        member_id = row.get('memberId', '').strip()
        state = row.get('state', '').strip()
        rating_regular = row.get('rating_regular', '').strip()
        rating_quick = row.get('rating_quick', '').strip()
        rating_blitz = row.get('rating_blitz', '').strip()
        
        print(f"{name[:34]:<35} {member_id:<12} {state:<6} {rating_regular:<10} {rating_quick:<10} {rating_blitz:<10}")
    
    print("=" * 120)


def print_csv_raw(csv_data):
    """
    Print CSV data in raw format
    
    Args:
        csv_data: CSV content as string
    """
    print("\n📄 CSV Data:\n")
    print(csv_data)


def main():
    """Main function"""
    # Default API URL (can be overridden)
    api_url = "http://localhost:3000"
    
    # Get player name from command line arguments
    if len(sys.argv) > 1:
        player_name = sys.argv[1]
    else:
        player_name = "Smith"
    
    # Get max results from command line arguments
    max_results = 10
    if len(sys.argv) > 2:
        try:
            max_results = int(sys.argv[2])
        except ValueError:
            print("Warning: Invalid max_results, using default value 10")
    
    print("=" * 60)
    print("🏁 Player Search API Client")
    print("=" * 60)
    print(f"API URL: {api_url}")
    print(f"Search term: {player_name}")
    print(f"Max results: {max_results}")
    print("=" * 60 + "\n")
    
    # Search for players (JSON response)
    print("1️⃣  Searching for players...")
    player_data = search_players(api_url, player_name, max_results)
    
    if player_data:
        print(f"\n📊 Results:")
        for i, player in enumerate(player_data.get('players', []), 1):
            name = player.get('name', '').replace('\n', ' ')
            member_id = player.get('memberId', '')
            state = player.get('state', '')
            rating = player.get('rating', '')
            
            print(f"  {i}. {name} (ID: {member_id}, State: {state}, Rating: {rating})")
    
    # Get CSV data
    print("\n2️⃣  Retrieving CSV data...")
    csv_data = export_csv(api_url, player_name, max_results)
    
    if csv_data:
        # Print as table
        print("\n3️⃣  Printing CSV data as table:")
        print_csv_table(csv_data)
        
        # Optionally print raw CSV
        print("\n4️⃣  Raw CSV data:")
        print_csv_raw(csv_data)
    
    print("\n" + "=" * 60)
    print("✅ Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()

