thonimport json

def parse_channel_data(channel_data):
    """
    Parse and process the channel data into a more useful structure.
    :param channel_data: Raw channel data (dict)
    :return: Processed channel data (dict)
    """
    parsed_data = {}
    parsed_data['channel_id'] = channel_data.get('channel_id')
    parsed_data['channel_name'] = channel_data.get('name')
    parsed_data['channel_description'] = channel_data.get('description')
    parsed_data['subscribers'] = channel_data.get('subscribers')
    return parsed_data

def parse_video_data(video_data):
    """
    Parse and process the video data into a more useful structure.
    :param video_data: Raw video data (list of dicts)
    :return: Processed video data (list of dicts)
    """
    parsed_videos = []
    for video in video_data:
        parsed_video = {
            'video_id': video.get('video_id'),
            'title': video.get('title'),
            'views': video.get('views'),
            'likes': video.get('likes')
        }
        parsed_videos.append(parsed_video)
    return parsed_videos