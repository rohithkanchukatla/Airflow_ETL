import os
import googleapiclient.discovery
import pandas as pd

def process_comments(response_items):
    comments = []
    for comment in response_items:
        author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
        publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
        comment_info = {'author': author, 'comment': comment_text, 'published_at': publish_time}
        comments.append(comment_info)
    print(f'Finished processing {len(comments)} comments.')
    
    # Convert comments list to DataFrame
    df = pd.DataFrame(comments)
    
    # Save DataFrame to CSV file
    df.to_csv(r'C:\Users\rohit\OneDrive\Desktop\comments.csv', index=False)
    print('Comments saved to comments.csv')

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "Youtube API key here"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet, replies",
        videoId="q8q3OFFfY6c"
    )
    response = request.execute()
    process_comments(response['items'])

if __name__ == "__main__":
    main()
