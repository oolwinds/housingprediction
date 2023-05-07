# House Price Prediction

### Problem Statement
Create a predictive model to estimate the median value of owner-occupied homes in the Boston area using a variety of features, including crime rate, education (pupil-teacher ratio), accessibility to employment centers (average commuting distance), and socioeconomic factors (percent of lower-status population). This model enables potential buyers and sellers to make informed decisions when entering the housing market and helps policymakers identify areas for improvement within the urban landscape.

### **The house prices prediction webapp can be accessed by clicking [here!](https://housingprediction.onrender.com/)**

### Technologies Used
1. Jupyter Notebook - Data Analysis & Modelling
2. VSCode 
3. Python virtual environment
4. Flask - Web App and website creation
5. Gunicorn - Hosting flask application 
6. Render - deploying the machine learning model as web service

### Languages
1. Python

### Data
Source : https://www.openml.org/search?type=data&status=active&id=531

Data Dictionary : http://lib.stat.cmu.edu/datasets/boston

### Workflow
![workflow](https://user-images.githubusercontent.com/130780065/236673452-0e0d4072-1418-4e40-9c58-4732f1c87b76.JPG)

### Data Analysis & Modelling
When I started this project, my first step was to dive into the dataset using Jupyter Notebook. I performed data analysis and modeling to understand patterns, trends, and outliers within the data. After cleaning and preprocessing the data, I split it into training and testing sets. Then, I selected an appropriate machine learning algorithm and used libraries like Scikit-learn and fine-tune the model. In the end, the best performing model was the fine-tuned Random Forest model. Once the model was trained, I used the Python pickle module to serialize the model for later use. This allowed me to save the trained model to a file, which could then be easily loaded in the Flask application to make predictions without the need to retrain the model.

![metrics](https://user-images.githubusercontent.com/130780065/236687756-dade5d12-b4fe-4da1-af69-0098602c61fd.JPG)

![download](https://user-images.githubusercontent.com/130780065/236688543-65b436a2-296e-45d9-a60a-3952176e03dc.png)

### VSCode
For this project, I decided to use VSCode as my code editor. To manage project dependencies and ensure reproducibility, I created a Python virtual environment.

### Flask 
Next, I built a Flask web application to serve as the user interface for my machine learning model. Flask is a great web framework for quickly creating web applications. I designed the front-end using basic HTML, CSS, and JavaScript and connected it to the Flask back-end, which processed user input and interacted with the machine learning model to make predictions.

### GUnicorn
To host the Flask application, I used Gunicorn (Green Unicorn) as a Web Server Gateway Interface (WSGI) server. Gunicorn is a more robust option compared to Flask's built-in development server and is suitable for production deployments.

### Render
Lastly, I deployed the machine learning web app on a platform like Render. Render offers a simple and efficient way to host web applications. I set up the application on Render by providing necessary information, such as the code repository, environment type (Python), and required build and runtime commands. Once deployed, the machine learning model was accessible as a web service, allowing users to interact with it and receive predictions.

### Summary
Despite being familiar with the data analysis and machine learning aspects, this project presented a unique opportunity to learn and apply new technologies and techniques. It was my first experience working with VSCode to build a Flask web application, using Gunicorn for hosting, and employing the pickling technique for model serialization. This project also gave me an opportunity to work with web development tools such as html & css. All in all, this end-to-end machine learning web app, which enables users to interact with the trained model through an engaging interface, serves as a valuable addition to my portfolio.
![app](https://user-images.githubusercontent.com/130780065/236688072-598dfa94-a7ec-49b1-8a48-2e5d35f209fd.JPG)

