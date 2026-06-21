from googleapiclient.discovery import build
from django.conf import settings


def get_youtube_service():
    api_key = getattr(settings, 'YOUTUBE_API_KEY', '')
    if not api_key:
        return None
    return build('youtube', 'v3', developerKey=api_key)


def search_videos(query, max_results=10):
    youtube = get_youtube_service()
    if not youtube:
        return []
    
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results,
        videoEmbeddable='true',
        videoSyndicated='true'
    )
    response = request.execute()
    
    video_ids = [item['id']['videoId'] for item in response.get('items', [])]
    
    # Verify embeddability for all results
    embeddable_ids = set()
    if video_ids:
        details_request = youtube.videos().list(
            part='status',
            id=','.join(video_ids)
        )
        details_response = details_request.execute()
        for item in details_response.get('items', []):
            if item['status'].get('embeddable', False):
                embeddable_ids.add(item['id'])
    
    results = []
    for item in response.get('items', []):
        video_id = item['id']['videoId']
        snippet = item['snippet']
        results.append({
            'video_id': video_id,
            'title': snippet['title'],
            'description': snippet['description'],
            'thumbnail': snippet['thumbnails']['high']['url'],
            'channel_title': snippet['channelTitle'],
            'published_at': snippet['publishedAt'],
            'embeddable': video_id in embeddable_ids,
            'embed_url': f'https://www.youtube.com/embed/{video_id}',
            'watch_url': f'https://www.youtube.com/watch?v={video_id}',
        })
    return results


def get_video_details(video_id):
    youtube = get_youtube_service()
    if not youtube:
        return None
    
    request = youtube.videos().list(
        part='snippet,contentDetails,statistics,status',
        id=video_id
    )
    response = request.execute()
    
    items = response.get('items', [])
    if not items:
        return None
    
    item = items[0]
    snippet = item['snippet']
    content_details = item.get('contentDetails', {})
    statistics = item.get('statistics', {})
    status_info = item.get('status', {})
    embeddable = status_info.get('embeddable', True)
    
    return {
        'video_id': video_id,
        'title': snippet['title'],
        'description': snippet['description'],
        'thumbnail': snippet['thumbnails']['high']['url'],
        'channel_title': snippet['channelTitle'],
        'published_at': snippet['publishedAt'],
        'duration': content_details.get('duration', ''),
        'view_count': statistics.get('viewCount', '0'),
        'like_count': statistics.get('likeCount', '0'),
        'embeddable': embeddable,
        'embed_url': f'https://www.youtube.com/embed/{video_id}',
        'watch_url': f'https://www.youtube.com/watch?v={video_id}',
    }