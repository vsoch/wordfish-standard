# Wordfish Standard

This is an example data set for the [wordfish](http://www.github.com/radinformatics/wordfish) image and text annotation and markup application. For details about the database and API, please refer to that format. Details about the flat file structure are also included below, specifically to describe the data in this example.


Mammography dicom images with annotation document. Each example is uniquely identified by the combination of record_id and side (L or R) and will consist of two views - denoted CC and MLO in the name. The three categories for the thirteen dimensions are P (Pass), M(Marginal), F(Fail). In the ground truth spreadsheet that is in the folder all missing cells denote a Pass. This directory should have three of the examples from the ground truth label spreadsheet.

The folder [data](data) is expected to be compressed into a `.zip` or `.tar.gz`, as in [data.tar.gz](data.tar.gz). The name of this folder does not matter, but rather the contents inside. Any json file in the top level of the folder, named equivalently as the folder, is treated as custom metadata for the collection, and must be valid json. Specifically, any zipped up object corresponds to the level of a "collection" in the WordFish database, which can include images and/or text. 


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


## Folder Hierarchy
In the example above, Wordfish will obtain the unique identifiers for objects (entities) from the folders on the level of `entity`. Within each entity, it is required to have a folder called `images` and a folder called `text`, and all custom metadata about the entity must be in json file named with the equivalent entity identifier. The user has total freedom to specify what data goes in the custom metadata file, however it must be valid json.


### Images and Text
Image unique identifiers are stored on the level of `image*`, and text unique identifiers on the level of `text*` If an image and text correspond to the same occurrence, they should be named equivalently (with different extension). For each image and text, the same rule applies with regard to metadata - a json file is allowed with the corresponding name that must be valid json. 
