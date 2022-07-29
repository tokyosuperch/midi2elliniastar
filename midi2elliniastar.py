import pretty_midi
import sys
import os
import errno

class MultipleTrackException(Exception):
    pass

class Midi2ElliniaStar:
    FIRST_NOTENUM = 0
    PAGE_CHANGE_DELTA = 0.2
    ELLINIA_NOTENUM_OFFSET = 48
    ELLINIA_NOTETIME_RATIO = 10

    # Constructor
    def __init__(self, src_path):
        if not os.path.exists(src_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), src_path)
        self.midi_obj = pretty_midi.PrettyMIDI(src_path)
        self.converted_text = ""
        self.drift = 0
        self.midi_tracks = None

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
                note = notes[i]
                # Page Change check
                if i > self.FIRST_NOTENUM:
                    previous_note = notes[i-1]
                    if self.__is_page_change(note, previous_note):
                        self.converted_text += self.__rest_text(previous_note) + "\n"
                # Add note
                self.converted_text += self.__note_text(note) + "\n"

    # Checks if the guide-melody bar page can be changed
    def __is_page_change(self, note, previous_note) -> bool:
        return note.start - previous_note.end > self.PAGE_CHANGE_DELTA

    # Rest event text
    def __rest_text(self, previous_note) -> str:
        start_in_ellinia = self.__ellinia_note_time(previous_note.end)
        return "- " + str(start_in_ellinia)
    
    # Note event text
    def __note_text(self, note) -> str:
        start_in_ellinia = self.__ellinia_note_time(note.start)
        duration_in_ellinia = self.__ellinia_note_duration(note.duration)
        pitch_in_ellinia = self.__ellinia_pitch(note.pitch)
        return ": " + str(start_in_ellinia) + " " + str(duration_in_ellinia) + " " + str(pitch_in_ellinia)

    def __ellinia_note_time(self, time) -> int:
        return (time - self.drift) * self.ELLINIA_NOTETIME_RATIO

    def __ellinia_note_duration(self, duration) -> int:
        return duration * self.ELLINIA_NOTETIME_RATIO

    def __ellinia_pitch(self, pitch) -> int:
        return pitch - self.ELLINIA_NOTENUM_OFFSET

    # Create footer text
    def __create_footer(self):
        self.converted_text += "E"

def main():
    converter = Midi2ElliniaStar(sys.argv[1])
    result = converter.convert()
    print(result)

if __name__ == '__main__':
    main()
