from pytube import YouTube

def down():
    url = input("URL Download: ")
    yt = YouTube(f'{url}')
    print(yt.title)
    print(yt.thumbnail_url)

    yt = YouTube(
        f'{url}',
        use_oauth=False,
        allow_oauth_cache=True
    )

    yt = yt.streams
    ys = yt.get_highest_resolution()
    ys.download()

    print("Download Concluído. ")








