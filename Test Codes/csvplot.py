from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

solar_irradiation,voltage,temparature,power=np.loadtxt('s.csv',
				unpack=True,
				delimiter=',')

print(solar_irradiation)
print(power)
plt.plot(solar_irradiation,power)
#plt.plot(temparature,power)
plt.title('Solar cell Output(1000 ohm load)')
plt.xlabel('power')
plt.ylabel('irradiation')

plt.show()