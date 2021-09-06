from __future__ import unicode_literals
import youtube_dl



ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],

}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/playlist?list=PLlG4_DEZ0sFor9sYC1Oq4POQZXS_heEBp'])

# -o "/home/user/videos/%(title)s-%(id)s.%(ext)s"


# --playlist-items ITEM_SPEC


# --playlist-reverse                   Download playlist videos in reverse
#                                      order


# --playlist-random                    Download playlist videos in random
#                                      order


# -i, --ignore-errors                  Continue on download errors, for
#                                      example to skip unavailable videos in a
#                                      playlist


# --audio-format FORMAT                Specify audio format: "best", "aac",
#                                      "flac", "mp3", "m4a", "opus", "vorbis",
#                                      or "wav"; "best" by default; No effect
#                                      without -x


