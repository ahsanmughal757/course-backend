import yt_dlp
import json

def format_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}h {minutes}m {seconds}s" if hours else f"{minutes}m {seconds}s"

def get_playlist_data(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': False,
        'force_generic_extractor': False,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)
    
    playlist_title = playlist_info.get('title', 'Unknown')
    channel_name = playlist_info.get('uploader', 'Unknown')
    total_duration = sum(entry.get('duration', 0) for entry in playlist_info['entries'])
    
    lessons = []
    for entry in playlist_info['entries']:
        lessons.append({
            "title": entry.get('title', 'Unknown'),
            "duration": format_duration(entry.get('duration', 0)),
            "videoId": entry.get('id', 'Unknown')
        })
    
    course_data = {
        "id": 1,
        "userId": "21jdasku21",
        "title": playlist_title,
        "instructor": channel_name,
        "description": f"A basic crash course covering {playlist_title} by {channel_name}.",
        "videoId": lessons[0]['videoId'] if lessons else "Unknown",
        "videoUrl": f"https://www.youtube.com/watch?v={lessons[0]['videoId']}" if lessons else "Unknown",
        "prerequisites": ["A PC or Laptop with an internet connection."],
        "modules": [
            {
                "title": playlist_title,
                "description": f"A series of lectures covering various {playlist_title} topics.",
                "lessons": lessons
            }
        ],
        "duration": format_duration(total_duration),
        "level": "Intermediate",
        "category": "web-development",
        "rating": 4.8,
        "students": 12543
    }
    
    return json.dumps(course_data, indent=4)