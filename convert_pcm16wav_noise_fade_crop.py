import sys
import wave
import numpy as np
import random

file_name = sys.argv[1]
start_sample = int(sys.argv[2])
end_sample = int(sys.argv[3])
rnd_min = int(sys.argv[4])
rnd_max = int(sys.argv[5])
num_fade_in = int(sys.argv[6])
num_fade_out = int(sys.argv[7])
out_file_name = sys.argv[8]

num_samples = end_sample - start_sample

with wave.open(file_name, "rb") as wf:
    wf_channels = wf.getnchannels()  # チャンネル数
    wf_framerate = wf.getframerate()  # サンプリング周波数
    wf_n_frames = wf.getnframes()  # 全フレーム数
    wf_sample_width = wf.getsampwidth()  # バイト数 (16bitなら2)
    print(wf_channels, wf_framerate, wf_n_frames, wf_sample_width)
    wf_data = wf.readframes(wf_n_frames)

# 16bitの場合は 'int16'
audio_data_np = np.frombuffer(wf_data, dtype=np.int16) # 16bitの前提となっており現時点ではハードコードされておる
audio_data_edit = np.copy(audio_data_np[start_sample*wf_channels:end_sample*wf_channels])

# 他にマシな方法があるはずだが配列に対して順番な処理内容を簡単にわかりやすくするため愚直にループとifで処理
# add noise and fade-in/out
for xx in range(num_samples):
    for yy in range(wf_channels):
        current_samp_val = int(audio_data_edit[xx*wf_channels+yy]) + random.randint(rnd_min, rnd_max)
        if (xx < num_fade_in):
            current_samp_val = current_samp_val * xx / num_fade_in
        if (xx >= (num_samples - num_fade_out)):
            current_samp_val = current_samp_val * (num_fade_out - xx) / num_fade_out
        if (current_samp_val > 32767): # 符号付き16ビット整数の場合
            current_samp_val = 32767
        if (current_samp_val < -32768):
            current_samp_val = -32768
        audio_data_edit[xx*wf_channels+yy] = current_samp_val
# floating point values are cast to NumPy int16 type truncated towards zero
# Fade in and out after adding noise

with wave.open(out_file_name, "wb") as wf:
    wf.setnchannels(wf_channels)
    wf.setsampwidth(wf_sample_width)
    wf.setframerate(wf_framerate)
    wf.writeframes(audio_data_edit.tobytes())

# reference
# https://qiita.com/Oka_D/items/34e9f6c47962f51946c1
# https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html
# https://docs.python.org/ja/3/library/wave.html

