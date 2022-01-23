from . import models
import time
from googleapiclient.discovery import build
import threading


def youtube_search(query, max_results):
    api_keys = models.APIKey.objects.filter(is_limit_over=False)
    if len(api_keys) == 0:
        return {}
    DEVELOPER_KEY = api_keys[0]
    YOUTUBE_API_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    try:
        youtube_object = build(YOUTUBE_API_NAME,
                               YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        keyword = youtube_object.search().list(
            q=query, part="id, snippet", maxResults=max_results).execute()

        results = keyword.get("items", [])
    except:
        api_keys[0].is_limit_over = True
        api_keys[0].save()
        return {}
    return results


def get_desired_video(result):
    for i in range(len(result)):
        if 'videoId' in result[i]['id']:
            video_id = result[i]['id']['videoId']
        else:
            video_id = ''
        data = {
            'index': i,
            'video_title': result[i]["snippet"]["title"],
            'description': result[i]['snippet']['description'],
            'thumbnails_urls': result[i]['snippet']['thumbnails']['default']['url'],
            'video_id': video_id,
            'channel_id': result[i]['snippet']['channelId'],
            'publishing_date_time': result[i]['snippet']['publishedAt'],
        }
        obj = models.Video(**data)
        obj.save()


def time_of_most_recent_uploaded_video():
    recent_date_time = ''
    search_results = youtube_search('cricket', 10)

    if search_results == {}:
        return

    for result in search_results:
        video_date_time_obj = (
            result['snippet']['publishedAt'])
        insert_in_database(result)
        if not recent_date_time:
            recent_date_time = video_date_time_obj

        recent_date_time = max(recent_date_time, video_date_time_obj)
    return recent_date_time


def insert_in_database(result):
    if 'videoId' in result['id']:
        video_id = result['id']['videoId']
    else:
        video_id = ''
    data = {
        'video_title': result["snippet"]["title"],
        'description': result['snippet']['description'],
        'thumbnails_urls': result['snippet']['thumbnails']['default']['url'],
        'video_id': video_id,
        'channel_id': result['snippet']['channelId'],
        'publishing_date_time': result['snippet']['publishedAt'],
    }
    obj = models.Video(**data)
    obj.save()


def search_and_add_youtube_videos():
    recent_date_time = time_of_most_recent_uploaded_video()
    while True:
        search_results = youtube_search('cricket', 10)

        if len(search_results) == 0:
            return

        for result in search_results:
            video_date_time_obj = (
                result['snippet']['publishedAt'])
            try:
                if recent_date_time < video_date_time_obj:
                    insert_in_database(result)
                    recent_date_time = video_date_time_obj
            except:
                pass


def add_videos_continously():
    while True:
        api_keys = models.APIKey.objects.filter(is_limit_over=False)
        if len(api_keys) != 0:
            (search_and_add_youtube_videos())
        else:
            break
        time.sleep(10)


THREAD = threading.Thread(target=add_videos_continously)
