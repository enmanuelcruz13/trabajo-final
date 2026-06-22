from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.conf import settings
from django.core.cache import cache
import hashlib

CACHE_TTL = 86400  # 24 hours


def _cache_key(prefix, value):
    h = hashlib.md5(value.encode('utf-8')).hexdigest()
    return f'yt_{prefix}_{h}'


def get_youtube_service():
    api_key = getattr(settings, 'YOUTUBE_API_KEY', '')
    if not api_key:
        return None
    return build('youtube', 'v3', developerKey=api_key)


def search_videos(query, max_results=10):
    cache_key = _cache_key('search', f'{query}_{max_results}')
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    youtube = get_youtube_service()
    if not youtube:
        return []

    try:
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results,
            videoEmbeddable='true',
            videoSyndicated='true',
            relevanceLanguage='es',
            regionCode='MX'
        )
        response = request.execute()

        video_ids = [item['id']['videoId'] for item in response.get('items', [])]

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
        cache.set(cache_key, results, CACHE_TTL)
        return results
    except HttpError:
        return []
    except Exception:
        return []


def get_video_details(video_id):
    cache_key = _cache_key('details', video_id)
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    youtube = get_youtube_service()
    if not youtube:
        return None

    try:
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

        result = {
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
        cache.set(cache_key, result, CACHE_TTL)
        return result
    except HttpError:
        return None
    except Exception:
        return None
