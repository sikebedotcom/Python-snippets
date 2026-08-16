import sys
import wave
import numpy as np

file_name = sys.argv[1]
start_sample = int(sys.argv[2])
end_sample = int(sys.argv[3])
rnd_max = int(sys.argv[4])
rnd_min = int(sys.argv[5])
num_fade_in = int(sys.argv[6])
num_fade_out = int(sys.argv[7])
out_file_name = sys.argv[8]

# 全部の場合はどうする
num_samples = end_sample - start_sample + 1

with wave.open(file_name, "r") as wf:
    wf_channels = wf.getnchannels()  # チャンネル数
    wf_framerate = wf.getframerate()  # サンプリング周波数
    wf_n_frames = wf.getnframes()  # 全フレーム数
    wf_sample_width = wf.getsampwidth()  # バイト数 (16bitなら2)
    print(wf_channels, wf_framerate, wf_n_frames, wf_sample_width)
    wf_data = wf.readframes(wf_n_frames)

# 16bitの場合は 'int16'
audio_data_np = np.frombuffer(wf_data, dtype=np.int16)
audio_data_edit = np.copy(audio_data_np[start_sample*wf_channels:end_sample*wf_channels])

# add noise and fade-in/out
for xx in range(num_samples):
    for yy in range(wf_channels):
        current_samp_val = audio_data_edit[xx*wf_channels+yy] + random.randint(rnd_min, rnd_max)
        if (xx < num_fade_in):
            current_samp_val = current_samp_val * xx / num_fade_in
        if (xx > (num_samples - num_fade_out)):
            current_samp_val = current_samp_val * (num_fade_out - xx) / num_fade_out
        audio_data_edit[xx*wf_channels+yy] = current_samp_val
# WHY: div / or //

with wave.open(out_file_name, "w") as wf:
    wf.setnchannels(wf_channels)
    wf.getsampwidth(wf_sample_width)
    wf.setframerate(wf_framerate)
    wf.writeframes(audio_data_edit.tobytes())

# reference
# https://qiita.com/Oka_D/items/34e9f6c47962f51946c1
# https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html
# https://docs.python.org/ja/3/library/wave.html

