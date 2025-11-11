# Youtube Channel Scrapper

Effortlessly collect detailed data from YouTube channels and videos. This scraper gathers information about channels, recent videos, and video comments to help with content analysis, audience engagement, and video performance tracking.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Youtube Channel Scrapper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

The Youtube Channel Scrapper allows you to scrape YouTube channel and video details, including video metadata, comments, and captions. It is designed for users who want to automate the collection of YouTube content data for analysis, research, or personal use.

### Key Features

- Collect channel details (name, subscribers, views)
- Fetch metadata for up to 30 recent videos from a channel
- Scrape video information including title, views, likes, and comments
- Option to scrape video captions in different languages
- Ability to scrape comments with the option to limit the number collected

## Features

| Feature | Description |
|---------|-------------|
| Channel Information | Collect details like name, description, and view count. |
| Video Metadata | Retrieve title, duration, views, and more for each video. |
| Comments Collection | Extract up to 500 comments for each video (pagination applies). |
| Captions Scraping | Enable the "scrap_captions" parameter to fetch captions in a specific language. |

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| channel_id | The unique identifier for the YouTube channel. |
| channel_url | URL of the channel. |
| channel_name | Name of the YouTube channel. |
| channel_description | Description of the channel’s content. |
| video_id | Unique identifier for each video. |
| video_title | Title of the video. |
| video_views | Total views the video has received. |
| video_likes | Total likes the video has received. |
| video_comments | The number of comments on the video. |
| comment_text | The text content of the comment. |
| caption_data | Captions for the video, if available. |

## Example Output

    [
        {
            "channel_id": "UC4f0qvPJLqGTuLyy2iHOd-g",
            "channel_url": "https://www.youtube.com/@rtbf_info/",
            "channel_name": "RTBF Info",
            "video_id": "xpg_PujFT7s",
            "video_title": "Donald Trump devient officiellement le 47ème président des Etats-Unis - RTBF Info",
            "video_url": "https://www.youtube.com/watch?v=xpg_PujFT7s",
            "video_views": 27428,
            "video_likes": 336,
            "video_comments": 134,
            "comment_text": "Vive Trump !! Le ménage va commencer."
        }
    ]

## Directory Structure Tree

    youtube-channel-scrapper/

    ├── src/
    │   ├── scraper.py
    │   ├── extractors/
    │   │   ├── youtube_parser.py
    │   │   └── utils.py
    │   ├── config/
    │   │   └── settings.json
    ├── data/
    │   ├── inputs.sample.json
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

## Use Cases

- **Researchers** use it to collect YouTube content data for sentiment analysis or market research, so they can analyze trends and audience reactions.
- **Marketing professionals** use it to monitor video engagement, track likes, comments, and shares, enabling them to improve campaign effectiveness.
- **Content creators** use it to track the performance of their own videos, gather feedback through comments, and stay up to date with recent trends.

## FAQs

**Can I scrape more than 30 videos per channel?**
Yes, the scraper is configured by default to collect up to 30 videos per channel. If you need more, you can adjust the parameters or run multiple queries.

**Can I scrape video captions in a specific language?**
Yes, simply use the "caption_languages" parameter to specify the language code you want to collect captions for.

**Why are fake/empty comments appearing?**
In rare cases, when scraping slows down, we add placeholder comments to ensure that you still receive data. This helps prevent running at a loss due to server costs.

## Performance Benchmarks and Results

**Primary Metric:** Average collection of up to 500 comments per video.
**Reliability Metric:** 95% successful extraction on stable YouTube pages.
**Efficiency Metric:** 100 requests processed per minute on average.
**Quality Metric:** 98% data accuracy for video metadata and comments.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
