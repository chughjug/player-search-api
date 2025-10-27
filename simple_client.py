#!/usr/bin/env python3
"""
Simple Player Search API Client
Calls the API and prints CSV data
"""

import requests
import sys


def get_csv_from_api(api_url, player_name, max_results=10):
    """
    Call the API and get CSV data
    
    Args:
        api_url: Base URL of the API (e.g., "http://localhost:3000" or GitHub Pages URL)
        player_name: Name to search for
        max_results: Maximum number of results to return
    
    Returns:
        str: CSV content
    """
    # Build the export URL
    url = f"{api_url}/api/export"
    params = {
        "name": player_name,
        "max": max_results
    }
    
    print(f"🔍 Searching for: {player_name}")
    print(f"📡 Calling: {url}")
    print(f"📋 Parameters: {params}\n")
    
    try:
        # Make the API call
        response = requests.get(url, params=params, timeout=60)
        response.raise_for_status()
        
        # Get CSV data
        csv_data = response.text
        
        print(f"✅ Success! Received {len(csv_data)} bytes\n")
        print("=" * 80)
        print("📄 CSV DATA:")
        print("=" * 80)
        print(csv_data)
        print("=" * 80)
        
        return csv_data
        
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The server may be processing a large search.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None


def main():
    """Main function"""
    # Get player name from command line, default to "Smith"
    player_name = sys.argv[1] if len(sys.argv) > 1 else "Smith"
    
    # API URL - change this to your actual API URL
    # For local testing: "http://localhost:3000"
    # For production: your actual server URL or GitHub Pages URL
    api_url = "http://localhost:3000"
    
    print("=" * 80)
    print("🎯 Player Search API Client - Simple Version")
    print("=" * 80)
    print(f"🌐 API URL: {api_url}")
    print(f"👤 Player Name: {player_name}")
    print("=" * 80 + "\n")
    
    # Call the API and get CSV data
    csv_data = get_csv_from_api(api_url, player_name)
    
    if csv_data:
        print("\n✅ CSV data retrieved successfully!")
    else:
        print("\n❌ Failed to retrieve CSV data")
        sys.exit(1)


if __name__ == "__main__":
    main()

