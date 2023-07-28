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
'''
x.shape[-1]は、NumPy配列xの最後の軸（要素数）を返します。
この軸は、サンプル数となります。
これは、DFTの結果として得られる周波数成分の数と同じです。
'''

'''np.fft.fftfreqは、NumPyのFFT（Fast Fourier Transform）モジュールに含まれる関数で、
DFTの結果として得られる周波数成分を表す周波数軸を作成するために使用されます。
この関数は、周期Tを指定しない限り、秒で表される周波数を返すようになっています。


'''

# 周波数成分の描画
plt.plot(frequency, y_dft_magnitude)
plt.xlabel('周波数 (Hz)')
plt.ylabel('振幅')
plt.show()
