import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_name = 'dyno_lab/16v-8in-slowpitch/StepTest_teamNick_16V_8in_slowpitch__2024-09-13_142313.csv'
df = pd.DataFrame(pd.read_csv(file_name))
X = (df['Time (s)']).to_list()[35:56]
Y = (df['Motor Optical Speed (RPM)']).to_list()[35:56]
max_Y = max(Y)
max_index = Y.index(max_Y)
target_Y = 0.632 * max_Y
plt.plot(X, Y, marker='o')

x_interp = np.interp(target_Y, Y[0:4], X[0: 4])
print("Tm: ", x_interp - X[1])

plt.axhline(y=max_Y, color='red', linestyle='--', label='$\omega_{ss}$ = '+f'{max_Y}')
plt.axhline(y=target_Y, color='red', linestyle='--', label='$\omega$ = 0.632$\omega_{ss}$ = '+f'{target_Y}')
plt.axvline(x=x_interp, color='blue', linestyle='--', label=f'$t_e$ = {x_interp:.3f}')
plt.axvline(x=X[1], color='blue', linestyle='--', label=f'$t_s$ = {X[1]:.3f}')
plt.scatter([x_interp], [target_Y], color='purple', zorder=5)

plt.title('Response Curve (16V-8in-normal)')
plt.xlabel('Time (s)')
plt.ylabel('Motor Optical Speed (RPM)')
plt.legend()
plt.grid()
plt.show()

