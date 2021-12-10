
import seaborn as sb
ir=sb.load_dataset("titanic")
sb.violinplot(x="fare",y="sex",data = ir)
import matplotlib as plt
plt.show()
             