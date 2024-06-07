#Decision Tree
from sklearn import tree
X=[[25,30,35],[60,55,55],[30,35,40],[65,70,50],[55,60,55],[35,35,30]]
Y=['female','male','female','male','male','female']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
prediciton=clf.predict([[60,35,30]])
print (prediciton)

#RandomForest

from sklearn.ensemble import RandomForestClassifier

X=[[25,30,35],[60,55,55],[30,35,40],[65,70,50],[55,60,55],[35,35,30]]
Y=['female','male','female','male','male','female']
clf=RandomForestClassifier()
clf=clf.fit(X,Y)
pre=clf.predict([[60,35,30]])
print(pre)

#GradientBoosting

from sklearn.ensemble import GradientBoostingClassifier

X=[[25,30,35],[60,55,55],[30,35,40],[65,70,50],[55,60,55],[35,35,30]]
Y=['female','male','female','male','male','female']
clf=GradientBoostingClassifier()
clf=clf.fit(X,Y)
pre=clf.predict([[60,35,30]])
print(pre)

from sklearn.ensemble import GradientBoostingRegressor

X=[[25,30,35],[60,55,55],[30,35,40],[65,70,50],[55,60,55],[35,35,30]]
Y=['0','1','0','1','1','0']
reg=GradientBoostingRegressor()
reg=reg.fit(X,Y)
pre=reg.predict([[60,35,30]])
print(pre)
if pre >= 0.5:
    print("male")
else :
    print("female")     


