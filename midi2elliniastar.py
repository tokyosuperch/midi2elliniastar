import pretty_midi
import sys
import os
import errno

def main():
    drift = 0
    src_path = sys.argv[1]
    if not os.path.exists(src_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), src_path)
    midi_obj = pretty_midi.PrettyMIDI(src_path)
    end_time = midi_obj.get_end_time()
    midi_tracks = midi_obj.instruments
    print("#TITLE:")
    print("#MP3:song.ogg")
    print("#COVER:cover.png")
    print("#BACKGROUND:cover.png")
    print("#VIDEO:video.mp4")
    print("#BPM:150")
    for track in midi_tracks:
        notes = track.notes
        for i in range(len(notes)):
            if i > 0:
                if notes[i].start - notes[i-1].end > 0.2:
                    print("- " + str((notes[i-1].end - drift) * 10))
            print(": " + str((notes[i].start - drift) * 10) + " " + str(notes[i].duration * 10) + " " + str(notes[i].pitch - 48))
    print("E")

if __name__ == '__main__':
    main()
