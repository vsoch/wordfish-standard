# Wordfish Standard

This is a simple standard that describes an organization of images and text, intended for open source applications like [docfish](http://www.github.com/vsoch/docfish) for general image and text annotation. The WordFish standard is also used by the Stanford Open Modules for Python ([som](https://github.com/vsoch/som)), which drive the core functions of this application. For details about the database and API, please refer to that format. Details about the flat file structure are also included below, specifically to describe the data in this example.


## Machine Learning with Cookie Tumors

### Candy Tumors: The Training Set
The folder [cookies](examples/demo1) is an example of a collection, meaning a set of entities with images and text. In this case, this is our training set, so you will find candy "tumors" that are commonly found in cookies, and they include features like size and color, along with class labels. You might be interested in training a classifier to predict the tumor class based on the image features provided, or features extracted on your own using the provided overlay masks. 

### Cookie Patients: The Testing Set
If you look in [examples](examples) you will find the [cookie-tumor](examples/demo2) dataset, and this is the testing set. Here we have our poor cookie patients, each riddled with cookie tumors, and they badly need a diagnosis! Can you use your classifier to diagnose them?


### Medical Images
If you look in [examples](examples/demo3) you will find a more traditional radiology dataset, in the same format.


## The WordFish Standard:
It can be used as a folder, or compressed into a `.zip` or `.tar.gz`, as in `cookies.tar.gz`. The name of this folder does not matter, but rather the contents inside. Any json file in the top level of the folder, named equivalently as the folder, is treated as custom metadata for the collection, and must be valid json. Specifically, any zipped up object corresponds to the level of a "collection" in the WordFish database, which can include images and/or text. 


```bash
  data/   
      data.json
      entity1/
      entity2/
          images/
             image1/
                  image1.json
                  image1.png
                  overlay1.png
             image2/
          text/
             text1/
             text2/
                 text2.json
                 text2.txt              
          entity2.json
```

## Folder Hierarchy
In the example above, Wordfish will obtain the unique identifiers for objects (entities) from the folders on the level of `entity`. Within each entity, it is required to have a folder called `images` and a folder called `text`, and all custom metadata about the entity must be in json file named with the equivalent entity identifier. The user has total freedom to specify what data goes in the custom metadata file, however it must be valid json.


### Images and Text
Image unique identifiers are stored on the level of `image*`, and text unique identifiers on the level of `text*` If an image and text correspond to the same occurrence, they should be named equivalently (with different extension). For each image and text, the same rule applies with regard to metadata - a json file is allowed with the corresponding name that must be valid json. 


# Examples

Here is a small working example, for a set of mammography images. In this case, the user has chosen to keep metadata about the images with the id, specifically the modality and orientation (left/right):

```bash
tree -R data/
data/
├── 1303348158021579
│   └── images
│       ├── 1303348158021579_CC_R.dcm
│       └── 1303348158021579_MLO_R.dcm
└── 3921125518197313
    └── images
        ├── 3921125518197313_CC_L.dcm
        ├── 3921125518197313_CC_R.dcm
        ├── 3921125518197313_MLO_L.dcm
        └── 3921125518197313_MLO_R.dcm
```
