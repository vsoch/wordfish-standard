# Candy Tumor Collection

This is an example of a candy tumor collection, meaning a set of images (without any metadata or annotation beyond an image id) that has been formatted into the WordFish Standard. The collection can be found in [candy-tumor](candy-tumor) and the preparation of it for Wordfish in [prep](prep). This dataset is akin to any kind of imaging set that we want to classify based on its features. In this case, the features are candy, and they are embedded in cookies as "tumors" to make the task harder. This is similar to medical imaging, except we have much more information by way of having color. What is your task?

## Preparation Tasks

 1. Prepare both cookie tumor testing and training data, format into WordFish datasets
 2. Upload to WordFish
 3. For images, use Image Description annotation tool to get radiologist descriptions of tumors
 4. For images, use Image Markup for individuals to outline important parts of images. Either see how similar comes to "ground truth" ROI, or use to generate new ROI's for dataset that does not have them (and still show comparison to ground truth).
 5. For images, use Image Annotation to upload classes, and annotate (unlabeled) with ground truth
 6. Export datasets with both text and images, and add to Kaggle for machine learning fun! (see below)


## Possible Tasks

### 1. Predict Cookie Tumors from Images
Use the image features and classes described in the [demo](demo) as a training set. You want to predict the cookie classes in [cookie-tumor](examples/cookie-tumor) based on their features. The gold standard (correct labels) come by way of WordFish, but will not be provided with the dataset. The highest accuracy wins.

### 2. Predict Cookie Tumors From Text
Do the same as above, but use the radiologist reports (text) to predict the cookie tumors.

### 3. Predict Cookie Tumors From Text and Images
Use both images and text.

### 4. Remove Information
Try making the images black and white first (to mimic a radiograph) and try the task.

### 5. Predict the Patient
Train a classifier to group the images based on the "patient," or images of the same cookie.


For all of the above, your accuracy will be assessed also based on the difficulty of the image.

More to come!
