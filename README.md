![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Cherry Leaves Project
## Introduction
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

### Hypothesis and how to validate?

* By reducing the manual process of testing leaves, the client can save time using the ML model and therefore test more in a given time. 

### Business Requirements
1. The client is interested in having a study to visually differentiate between healthy and diseased leaves.
2. The client is interested in telling whether a specific leaf has mildew or not. 

### The rationale to map the business requirements to the Data Visualisations and ML tasks

The following User Stories were created and this is how they applied to each business requirement. (The number represents to the User Story number)
#### User Stories applicable to Business Requirement 1
1. As a data collector, I can collect the images of leaves so that I can differentiate between healthy and diseased cherry leaves.
2. As a data analyst, I can clean the data by removing non-images so that I do not have data that is not compatible with this project.
3. As a data analyst, I can display images so that I can show the customer the data set of leaves.
4. As a data analyst, I can augment the data so that I can the model can be trained with different types of images since not all images will be from the same angle.

#### User Stories applicable to Business Requirement 2
5. As a Machine Learning Engineer, I can create a classification model so that I can predict the classification of a leaf and class it as healthy or diseased.
6. As a machine learning engineer, I can train the model so that it can find a patterns in the dataset.
7. As a machine learning engineer, I can test the model so that I can make sure the model can also find patterns in data it has not seen before
8. As a Machine Learning Product Manager, I can design a dashboard so that I can display the data to my client as per the business requirements.
9. As a Machine Learning Project Manager, I can develop the dashboard so that I can present the data to client.

#### User Story applicable to both Business Requirements
10. As a client, I can use the dashboard so that I can quickly and accurately tell if a tree has diseased or healthy leaves.

## ML Business Case
* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

### Goals
* To increase the speed of the testing of leaves. 
* Reduce the manual process of finding specifically diseased leaves.
* Have a higher degree of accuracy compared to manual testing. 

### User Demographic
This project started because of farmers. However, it can be used also for the following 
* Park Rangers
* Wildlife Experts
* Amateur Wildlife Enthusiasts

## Features

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).
  
## Manual Testing

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.


## Credits
### Code
#### split-folders
I was struggling to split my data set into Train, Validation and Test sets. Therefore, I used [this](https://stackoverflow.com/questions/57394135/split-image-dataset-into-train-test-datasets) Stack Overflow post or specifically [this answer](https://stackoverflow.com/a/63118451). I learnt how to use split-folders which was a quicker way to split your data. However, it should be noted that it is encouraged to use the longer method since this shows exactly how splitting the data works. I would recommend split-folders to anyobdy who wants to work efficiently. The code in the specific post was edited to work with my project.

#### Git push
At one point early on, my code would not push to my repository. To troubleshoot, I search the internet and found [this](https://stackoverflow.com/questions/45293263/git-updates-were-rejected-because-the-tip-of-your-current-branch-is-behind) helpful Stack Overflow post. Despite it telling you the error message and how to rectify it in my terminal, I needed some extra information. In the end, I specifically used [this answer](https://stackoverflow.com/a/74548526). I felt it was okay to use this commanc since I was using it early in my project. 
### Content

* The text for the Home page was taken from Wikipedia Article A.
* Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

* The photos used on the home and sign-up page are from This Open-Source site.
* The images used for the gallery page were taken from this other open-source site.

## Main Data Analysis and Machine Learning Libraries

* This model is a classification model since the client would like to classify the images into healthy and unhealthy
## Unfixed Bugs

* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Acknowledgements (optional)

* Thank you to Code Institute for the Walkthrough Project (Malaria Detector) which I used for this project as well as the Streamlit calculator lessons

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Codeanywhere Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Codeanywhere Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use. 

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into <a href="https://app.codeanywhere.com/" target="_blank" rel="noreferrer">CodeAnywhere</a> with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and <code>pip3 install -r requirements.txt</code>

1. In the terminal type <code>pip3 install jupyter</code>

1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.


## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.






## Business Requirements



* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.



















