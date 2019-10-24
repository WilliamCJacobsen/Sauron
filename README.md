# Sauron
> As sauron this project makes your product see everything. So be aware, with great power comes great responsibility.

I use openCV to find and classify faces that I fed it. 

![](https://www.syfy.com/sites/syfy/files/styles/1200x680/public/wire/legacy/sauroneye.png)

## Installation

```sh
pip install pipenv
pipenv install
cd src
pipenv run python main.py
```

## Training
For this you need images of the individuals and place them inside a folder called pictures inside sauron directory. Inside this folder you'll need subfolders with names of the individuals placed inside. You can only use .png and .jpeg files. 

DECAPRECATED: 
To run the training add 
```
if __name__ == "__main__":
    the_eye = sauron()
    the_eye.train()
```
inside main.py

Usage of OpenCV is now decaprecated and will not be improved for later use. 
This is because of CNN networking usage. To feed the network please use different pictures of the target.

## Usage example

To classify members of a team. 

## Info

Uses CNN to classify the user. the result is softmax values. 
