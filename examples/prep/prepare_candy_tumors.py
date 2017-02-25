from glob import glob
import os
import re
import shutil
import simplejson
import exifread

pwd = os.getcwd()
output_dir = os.path.abspath("%s/../candy-tumor" %(pwd))

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

cookies = glob("%s/data/cookie*" %(pwd))
print("Found %s candy tumor entities." %(len(cookies)))

def parse_metadata(image_file,cookie_id):
    '''read_metadata uses exifread to read image header data
    '''
    metadata = []
    metadata.append(make_kv('id',cookie_id))
    metadata.append(make_kv('file',os.path.basename(image_file)))

    with open(image_file, 'rb') as filey:
        tags = exifread.process_file(filey)

    for tag,value in tags.items():
        if not re.search('Thumbnail',tag):
            value = str(value).replace(' ','')
            if len(value) > 0:
                metadata.append(make_kv(tag,value))

    return metadata


def write_json(json_obj,filename,mode="w",print_pretty=True):
    '''write_json will (optionally,pretty print) a json object to file
    :param json_obj: the dict to print to json
    :param filename: the output file to write to
    :param pretty_print: if True, will use nicer formatting   
    '''
    with open(filename,mode) as filey:
        if print_pretty == True:
            filey.writelines(simplejson.dumps(json_obj, indent=4, separators=(',', ': ')))
        else:
            filey.writelines(simplejson.dumps(json_obj))
    return filename



def make_kv(key,value):
    '''make_kv will return a dict
    with a key and value pair
    '''
    return {'key':key,'value':value}


# Main function is here, parsing the cookies!

for c in range(len(cookies)):

    cookie_path = cookies[c]
    
    # First find cookie images based on image files
    cookie_id = os.path.basename(cookie_path)
    cookie_dir = "%s/%s" %(output_dir,cookie_id)
    cookie_images = "%s/images" %(cookie_dir)
    if not os.path.exists(cookie_dir):
        os.mkdir(cookie_dir)
        os.mkdir("%s/images" %(cookie_dir))

    # For each image, copy to output directory along with metadata
    images = glob("%s/*.jpg" %(cookie_path))
    for i in range(len(images)):
        image = images[i]
        image_folder = "%s/image%s" %(cookie_images,i+1)
        if not os.path.exists(image_folder):
            os.mkdir(image_folder)
        shutil.copyfile(image,"%s/image%s.jpg" %(image_folder,i+1))
        cookie_metadata = parse_metadata(image,cookie_id)
        write_json(cookie_metadata,"%s/image%s.json" %(image_folder,i+1))
