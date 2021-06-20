# The Knots 🌀

The cyclones are irregular wind movements involving closed air circulation around a low pressure centre. This closed air circulation is caused by atmospheric disturbances over and above the earth’s surface, coupled with the earth’s ‘rotation which imparts to these disturbances a whirling motion.

> Cyclones are dangerous and every year many families and properties get affected due to this. We can't stop Mother Nature's Disaster, but we can surely be prepared for it. 

**We aim to solve and help the people by alerting them regarding the presence of cyclones and what's the speed of it and there by saving lives.**

## About the Project
* **Tech Used:** HTML, CSS, JS, Bootstrap, PyTorch, TorchVision, Geocoder, OpenWeatherMap API
* **Objective:** Image Based Cyclone Speed Prediction by retraining Pretrained Architecture and countermeasure generation based on speed based cyclone categorization.
* **Future Steps:-**
  * We can upscale The Knots by Integrating it with an Android / IOS Application hence making it easily accessible to all the masses. 
  * We can also provide Real Time Cyclone Tracks for early execution of the safety measures to be taken.
  * We can also Improve the predictive Accuracy of the Models by using High End Resources 

## Motivation
* **Speed-Pattern Correlation:** Manual techniques indicates the strong relationship between spatial patterns and cyclone intensity.
* **Improving Manual Task:** Visual inspection is manual, subjective, and often leads to inconsistent estimates.
* **Existence of Public Dataset:** Dataset of satellite images and wind speed prepared by the NASA IMPACT team and Radiant Earth Foundation.

## Process
![main_ppt_flow](https://user-images.githubusercontent.com/43719685/122669848-bedb8580-d1dc-11eb-92ce-67ff348c3714.jpg)

1. **Uploading and Pre-processing:** Uploading image of the cyclone and preprocessing it using Torchvision.
2. **Inference:** Passing transformed image to ResNet-101 model loaded over saved weights of training.
3. **Update the Results:** Determining cyclone type based on prediction  speed  and pass the values to Flask
4. **Suggestion Generation:** Generating safety measures based on cyclone category along with plots and description.
