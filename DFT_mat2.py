import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# 波形データ（例：正弦波）
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# 離散フーリエ変換
y_dft = np.fft.fft(y)
y_dft_magnitude = np.abs(y_dft)

# 周波数軸
frequency = np.fft.fftfreq(x.shape[-1])

# 周波数成分の抽出
frequency_component = y_dft[np.argmax(y_dft_magnitude)]

# 周波数成分の振幅と位相
amplitude = np.abs(frequency_component)
phase = np.angle(frequency_component)

# 結果の表示
print("Amplitude: ", amplitude)
print("Phase: ", phase)
