from glob import glob
import os
import shutil
import simplejson
import xmltodict


pwd = os.getcwd()
output_dir = "%s/collection" %(pwd)



if not os.path.exists(output_dir):
    os.mkdir(output_dir)

cookies = glob("%s/matched/img/*.png" %(pwd))

def read_xml(xml_file):
    '''read_xml reads an xml file and returns a dict
    '''
    with open(xml_file) as filey:
        doc = xmltodict.parse(filey.read())
    return doc


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


def extract_features(marks):
    features = []
    if isinstance(marks,list):
        for mark in marks:
            mark_features = []
            mark_features.append(make_kv('name',mark['@name']))
            mark_features.append(make_kv('type',mark['@variableType']))
            mark_features.append(make_kv('value',mark['#text']))
            if "@units" in mark:
                mark_features.append(make_kv('units',mark['@units']))
        features.append(mark_features)
    else:
        mark_features = []
        mark_features.append(make_kv('name',marks['@name']))
        mark_features.append(make_kv('type',marks['@variableType']))
        mark_features.append(make_kv('value',marks['#text']))
        if "@units" in marks:
            mark_features.append(make_kv('units',marks['@units']))
            features.append(mark_features)
    return features


def parse_xml(xml_file,root=None):
    '''parse_xml will iterate over an xml file
    and return as a dictionary
    '''
    if root == None:
        root = "CandyTumor"
    doc = read_xml(xml_file)
    metadata = []
    metadata.append(make_kv('id',doc[root]['@uniqueIdentifier']))
    metadata.append(make_kv('rx',doc[root]['ClassAnnotation']['@class']))
    marks = doc[root]['ClassAnnotation']['TumorAnnotation']
 
    if isinstance(marks,dict):
        features = extract_features(marks['TumorFeature'])
    else:
        features = []
        for mark in marks:
            new_features = extract_features(mark['TumorFeature'])
            features = features + new_features
    metadata.append(make_kv('features',features))
    return metadata


# Main function is here, parsing the cookies!

for cookie in cookies:
    
    # First find cookie images based on image files
    cookie_image = os.path.basename(cookie)
    cookie_id = os.path.splitext(cookie_image)[0]
    cookie_dir = "%s/%s" %(output_dir,cookie_id)
    cookie_images = "%s/images" %(cookie_dir)
    if not os.path.exists(cookie_dir):
        os.mkdir(cookie_dir)
        os.mkdir("%s/images" %(cookie_dir))
        os.mkdir("%s/images/image1" %(cookie_dir))
    shutil.copyfile(cookie,"%s/image1/image1.png" %(cookie_images))

    # Is there a matching overlay (mask?)
    cookie_overlay = "%s/matched/mask/%s" %(pwd,cookie_image)
    if os.path.exists(cookie_overlay):
        shutil.copyfile(cookie_overlay,"%s/image1/overlay1.png" %(cookie_images))

    # Is there metadata?
    cookie_xml = "%s/matched/%s.xml" %(pwd,cookie_id)
    if os.path.exists(cookie_xml):
        cookie_metadata = parse_xml(cookie_xml)
        write_json(cookie_metadata,"%s/image1/overlay1.json" %(cookie_images))


