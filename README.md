# midi2elliniastar
Converts Standard MIDI File to ElliniaStar Deluxe score  
Standard MIDI FileをElliniaStar Deluxeの譜面に変換します。

## Usage(EN)
```
usage: midi2elliniastar.py [-h] [-n TRACK_NUMBER] [-o OFFSET] filename

Converts Standard MIDI File to Ellinia Star Deluxe score.

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  -n TRACK_NUMBER, --track-number TRACK_NUMBER
  -o OFFSET, --offset OFFSET
```
If you use MIDI file with multiple tracks, please set input file's track number with -n <TRACK_NUMBER> option.

## 使用方法(JP)
```
usage: midi2elliniastar.py [-h] [-n TRACK_NUMBER] [-o OFFSET] filename

Converts Standard MIDI File to Ellinia Star Deluxe score.

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit ヘルプメッセージを表示
  -n TRACK_NUMBER, --track-number TRACK_NUMBER トラック番号を指定
  -o OFFSET, --offset OFFSET 出力譜面に時間のずれを指定
```
複数トラックのあるMIDIファイルを使用する場合、-n <TRACK_NUMBER>オプションで入力ファイルのMIDIトラックを指定する必要があります。
