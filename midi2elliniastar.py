import pretty_midi
import sys
import os
import errno

class MultipleTrackException(Exception):
    pass

class Midi2ElliniaStar:

    converted_text = ""
    drift = 0
    midi_obj = None
    midi_tracks = None

    # Constructor
    def __init__(self, src_path):
        if not os.path.exists(src_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), src_path)
        self.midi_obj = pretty_midi.PrettyMIDI(src_path)

    def convert(self) -> str:
        self.midi_tracks = self.midi_obj.instruments
        # Execute convert
        self.__create_ellinia_string()
        return self.converted_text

    # Create whole score-file text
    def __create_ellinia_string(self):
        self.__create_header()
        self.__create_body()
        self.__create_footer()

    # Create header text
    def __create_header(self):
        header_key_values = [
            "#TITLE:", 
            "#MP3:song.ogg", 
            "#COVER:cover.png",
            "#BACKGROUND:cover.png",
            "#VIDEO:video.mp4",
            "#BPM:150"
        ]
        header_text = '\n'.join(header_key_values)
        self.converted_text += header_text + '\n'

    # Create score text
    def __create_body(self):
        for track in self.midi_tracks:
            notes = track.notes
            for i in range(len(notes)):
                if i > 0:
                    if notes[i].start - notes[i-1].end > 0.2:
                        self.converted_text += "- " + str((notes[i-1].end - self.drift) * 10) + "\n"
                self.converted_text += ": " + str((notes[i].start - self.drift) * 10) + " " + str(notes[i].duration * 10) + " " + str(notes[i].pitch - 48) + "\n"

    # Create footer text
    def __create_footer(self):
        self.converted_text.join("E")

def main():
    converter = Midi2ElliniaStar(sys.argv[1])
    result = converter.convert()
    print(result)

if __name__ == '__main__':
    main()
