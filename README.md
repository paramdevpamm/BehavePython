# BehavePython
Behave using Python
Once we clone the repo, open the folder in any IDE that supports python, here I am using PyCharm
Open Command promt and navigate to the Python project and run below command 
```behave -f allure_behave.formatter:AllureFormatter -o reports/ Feature/MyFeature.feature```

For Report generation run the below command
```allure serve reports\```

The report would be stored in ```reports``` folder
