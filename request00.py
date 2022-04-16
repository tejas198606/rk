import requests


url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':2.0,'cp':6.0,'trestbps':2.0,'chol':9.0,'fbs':6.0,'restecg':9.0,'thalach':6.0,'exang':2.0,
                            'oldpeak':9.0,'slope':6.0,'ca':6.0,'thal':9.0})

print(r.json()) ## we can give single value also  'age':2.0000, // 'age':2,


