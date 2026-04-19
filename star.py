import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
plt.style.use('dark_background')



fig, ax = plt.subplots()
x = np.random.rand(20)
y = np.random.rand(20)


scat = ax.scatter(x, y, s=35, c='white', alpha=0.5, marker='*') 
scat2 = ax.scatter(x, y, s=35, c='gold', alpha=0.5, marker='*') 

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_frame_on(False)
plt.axis('off')

def update(frame):
    nuevo_alpha = np.sin(frame / 30) ** 2 
    

    scat.set_alpha(nuevo_alpha)
    scat2.set_alpha(nuevo_alpha)
    

    scat.set_offsets(np.random.rand(5, 2))
    scat2.set_offsets(np.random.rand(5, 2))
    
    
    return scat, scat2



ani = animation.FuncAnimation(fig, update, frames=50, interval=260, blit=True)


plt.show()
