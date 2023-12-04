#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LRC to SubRip

During your most recent trip to Codelandia you decided to buy a brand new
CodePlayer, a music player that (allegedly) can work with any possible media
format. As it turns out, this isn't true: the player can't read lyrics written
in the LRC format. It can, however, read the SubRip format, so now you want to
translate all the lyrics you have from LRC to SubRip.

Since you are a pro programmer (no noob would ever get to Codelandia!), you're
happy to implement a function that, given lrcLyrics and songLength, returns the
lyrics in SubRip format.

Example

For

lrcLyrics = ["[00:12.00] Happy birthday dear coder,",
             "[00:17.20] Happy birthday to you!"]

and

songLength = "00:00:20", the output should be

solution(lrcLyrics, songLength) = [
    "1",
    "00:00:12,000 --> 00:00:17,200",
    "Happy birthday dear coder,",
    "",
    "2",
    "00:00:17,200 --> 00:00:20,000",
    "Happy birthday to you!"
]

Input/Output

lrcLyrics

Lyrics in LRC format. Each string has the format [MM:SS.xx] <song_line>, (note
the whitespace character after the time) where:

    MM:SS.xx is the lyrics time (it is guaranteed that the elements of lrcLyrics
    are sorted in ascending order of this time);
    0 ≤ int(xx) ≤ 99;
    0 ≤ int(SS) ≤ 59;
    0 ≤ int(MM) ≤ 99;
    <song_line> is the corresponding lyrics line.

songLength
The length of the song in the format "HH:MM:SS". It is guaranteed that it is
greater than the last time in lrcLyrics.

"""


def formatted_times_generator(raw_strings: list[str], final_time: str):
    all_times = []
    for line in raw_strings:
        seconds_frames_str = line[4:9].replace(".", ",") + "0"
        minutes_str = line[1:3]
        minutes = int(minutes_str)
        if minutes > 59:
            hours_str = str(minutes // 60).zfill(2)
            minutes_str = str(minutes % 60).zfill(2)
        else:
            hours_str = "00"
        all_times.append(":".join([hours_str, minutes_str, seconds_frames_str]))
    all_times.append(final_time + ",000")
    return iter(all_times)


def solution(lrc_lyrics: list[str], song_length: str) -> list[str]:
    formatted_times = formatted_times_generator(lrc_lyrics, song_length)

    subrip = []
    next_time = next(formatted_times)
    for line_number, line in enumerate(lrc_lyrics, 1):
        current_time = next_time
        next_time = next(formatted_times)
        subrip.append(str(line_number))
        subrip.append(f"{current_time} --> {next_time}")
        subrip.append(line[11:])
        subrip.append("")

    return subrip[:-1]


def main():
    lrc_lyrics = [
        "[00:12.00] Happy birthday dear coder,",
        "[00:17.20] Happy birthday to you!",
    ]
    song_length = "00:00:20"
    # expected = [
    #     "1",
    #     "00:00:12,000 --> 00:00:17,200",
    #     "Happy birthday dear coder,",
    #     "",
    #     "2",
    #     "00:00:17,200 --> 00:00:20,000",
    #     "Happy birthday to you!",
    # ]
    print(solution(lrc_lyrics, song_length))


if __name__ == "__main__":
    main()
