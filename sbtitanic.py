import seaborn as sb
ir=sb.load_dataset("titanic")
sb.swarmplot(x="age", y="fare",data=ir)
import matplotlib as plt
plt.show()
             