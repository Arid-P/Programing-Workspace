import os
import zipfile
import glob

def automate_chosen_playlists():
    # Detect current directory (Downloads folder)
    current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
    
    zip_pattern = os.path.join(current_dir, "takeout-*.zip")
    zip_files = glob.glob(zip_pattern)
    
    if not zip_files:
        print(f"Could not find a 'takeout-xxx.zip' file in: {current_dir}")
        return
    
    target_zip = max(zip_files, key=os.path.getmtime)
    print(f"Processing Takeout archive: {os.path.basename(target_zip)}\n")

    # Your exact whitelist from the terminal choices
    allowed_playlists = {
        "Favorite Songs",
        "Vibe Songs",
        "Bollywood Item Songs _ Hottest Hits",
        "Y5 (Y4+Sufr radio",
        "RMix1",
        "2026 is the new 2016",
        "Y8",
        "pureojiuice",
        "Y4",
        "Y9",
        "Bath",
        "Y6",
        "Temp 1",
        "SM1"
    }

    final_list = []

    with zipfile.ZipFile(target_zip, 'r') as archive:
        all_files = archive.namelist()
        
        # Pull out the playlist paths
        csv_paths = [f for f in all_files if "YouTube and YouTube Music/playlists/" in f and f.endswith('.csv')]

        for internal_path in csv_paths:
            filename = internal_path.split('/')[-1]
            playlist_name = filename.replace('.csv', '').replace('-videos', '')

            # If it's a playlist you wanted, process it
            if playlist_name in allowed_playlists:
                playlist_id = None
                
                try:
                    with archive.open(internal_path) as f:
                        content = f.read().decode('utf-8').splitlines()
                        
                        # Fallback parsing strategy: 
                        # Look inside the file for the playlist metadata block Google provides
                        for line in content:
                            if "Playlist ID" in line or "ID," in line:
                                parts = line.split(',')
                                if len(parts) > 1:
                                    playlist_id = parts[1].strip().strip('"')
                                    break
                except Exception:
                    pass

                # If Google Takeout omitted the ID row entirely, we use a programmatic fallback:
                # We will mark it so you can see it clearly, or reconstruct standard share links.
                if playlist_id:
                    share_link = f"https://music.youtube.com/playlist?list={playlist_id}"
                else:
                    # Fallback notice if Google completely decoupled the metadata from the zip archive
                    share_link = f"https://music.youtube.com/playlist?list=[Check_YouTube_Library_For_{playlist_name.replace(' ', '_')}]"

                final_list.append((playlist_name, share_link))

    # Print the clean final array
    print("========================================")
    print("       AUTOMATED CHOSEN PLAYLISTS       ")
    print("========================================")
    
    # Sort them to match your exact output ordering requirement
    order_map = {name: i for i, name in enumerate(allowed_playlists)}
    final_list.sort(key=lambda x: order_map.get(x[0], 99))

    string = ""
    for i, (name, link) in enumerate(final_list, 1):
        print(f"{i}. {name}")
        print(f"   Link: {link}")
        print("-" * 40)
        string += link 
        string += "\n"
    
    print("All the links: \n", string)

if __name__ == "__main__":
    automate_chosen_playlists()

