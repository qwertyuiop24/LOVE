def create_playlist():
    songs = [
        "Your Song by Elton John",
        "Perfect by Ed Sheeran",
        "All of Me by John Legend",
        "A Thousand Years by Christina Perri",
        "Thinking Out Loud by Ed Sheeran",
        "Just the Way You Are by Bruno Mars",
        "Can't Help Falling in Love by Elvis Presley",
        "I Don't Want to Miss a Thing by Aerosmith",
        "Lucky by Jason Mraz and Colbie Caillat",
        "You Are the Reason by Calum Scott"
    ]

    message = f"""
    My Dearest Misis Layson ko,

    Happy Monthsary! 🎉❤️

    To celebrate our special day, I’ve put together a playlist of songs that remind me of you and our amazing journey together. Each song holds a special place in my heart and tells a part of our story.

    Here are the songs for you:
    """

    for i, song in enumerate(songs, 1):
        message += f"{i}. {song}\n"

    message += """
    I hope you enjoy listening to it as much as I enjoyed creating it for you. Let these songs be a reminder of how much I love you and how excited I am for our future together.

    I love you so much, and I can’t wait to see you soon! 😘🎶

    Yours always,
    Soon-to-be your Husband
    """

    with open("playlist_message.txt", "w", encoding="utf-8") as file:
        file.write(message)

    print("Playlist and message created successfully!")

# Call the function to create the playlist and message
create_playlist()
