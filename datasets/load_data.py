# this class will load all the required data used for this project
# import necessary packages
import os
import progressbar
from shutil import  copyfile

class LoadData:
  @staticmethod
  def load():
    # define source directory to copy images from
    source = "/content/hirise-map-proj-v3_2/map-proj-v3_2/"
    # define classmaps
    classes = {
    "0": "other",
    "1": "crater",
    "2": "dark dune",
    "3": "slope streak",
    "4": "bright dune",
    "5": "impact ejecta",
    "6": "swiss cheese",
    "7": "spider"}

    # Load all 64k images with given train, val and test splits
    print("\n[INFO][1] Loading...")
    with open("/content/hirise-map-proj-v3_2/labels-map-proj_v3_2_train_val_test.txt") as f:
        data = f.read().split("\n")
        
        # define widgets for progressbar
        widgets = ["Copying files...:", progressbar.Percentage(), " ",
        progressbar.Bar(), " ", progressbar.ETA()]
        pbar = progressbar.ProgressBar(maxval=len(data), widgets=widgets).start()
        
        for i, image_label in enumerate(data):
            path = image_label.split(" ")
            image = path[0]
            if len(path) > 1:
                label = classes[path[1]]
                typ = path[-1]

                # define destination folder
                destination = "/content/splitted_data/{}/{}/".format(typ, label)

                # if destination folder does not exists create a new one
                if not os.path.exists(destination):
                    os.makedirs(destination)

                # copy file
                copyfile(source+image, destination+image)
                        
            pbar.update(i)
        pbar.finish()
        print("[INFO] Done...")

    # load all images with given split but excluding augmented images 
    # from "other" category
    print("\n[INFO][2] loading...")
    with open("/content/hirise-map-proj-v3_2/labels-map-proj_v3_2_train_val_test.txt") as f:
      data = f.read().split("\n")
        
      widgets = ["Copying files...:", progressbar.Percentage(), " ",
      progressbar.Bar(), " ", progressbar.ETA()]    
      pbar = progressbar.ProgressBar(maxval=len(data), widgets=widgets).start()
      
      for i, image_label in enumerate(data):
          path = image_label.split(" ")
          image = path[0]
          if len(path) > 1:
              label = classes[path[1]]
              typ = path[-1]
              
              # initialize destination folder name
              destination = "/content/train_test_split/{}/{}/".format(typ, label)
              
              # if label is "other" then only store non-augmented image
              if label == "other":
                  if len(image_label.split("-")) == 2:
                      # if destination folder does not exists create a new one
                      if not os.path.exists(destination):
                          os.makedirs(destination)                    
                      # copy file
                      copyfile(source+image, destination+image)
              else:
                  # if destination folder does not exists create a new one
                  if not os.path.exists(destination):
                      os.makedirs(destination)                    
                  # copy file
                  copyfile(source+image, destination+image)    

          pbar.update(i)
      pbar.finish()
      print("[INFO] Done...")

    # load images with excluding augmented images from "other" category
    # and keeping the train and val images together but the test set will remain
    # same and untouched
    print("\n[INFO][3] loading...")
    with open("/content/hirise-map-proj-v3_2/labels-map-proj_v3_2_train_val_test.txt") as f:
        data = f.read().split("\n")
        
        widgets = ["Copying files...:", progressbar.Percentage(), " ",
        progressbar.Bar(), " ", progressbar.ETA()]

        pbar = progressbar.ProgressBar(maxval=len(data), widgets=widgets).start()
        
        for i, image_label in enumerate(data):
            path = image_label.split(" ")
            image = path[0]
            if len(path) > 1:
                label = classes[path[1]]
                typ = path[-1]
                
                # initialize destination folder name for train and val (store in one folder)
                destination = "/content/dataset/train_val/{}/".format(label)

                if path[-1] == "test":
                  destination = "/content/dataset/test/{}/".format(label)
                
                
                if label == "other":
                    if len(image_label.split("-")) == 2:
                        # if destination folder does not exists create a new one
                        if not os.path.exists(destination):
                            os.makedirs(destination)

                        # copy file
                        copyfile(source+image, destination+image)
    #                 pass
                else:
                    # if destination folder does not exists create a new one
                    if not os.path.exists(destination):
                        os.makedirs(destination)

                    # copy file
                    copyfile(source+image, destination+image)

                        
            pbar.update(i)
        pbar.finish()
        print("[INFO] Done...")

  #   # EXTRACTING MSL DATA
  #   # define source path to copy file from
    source = "/content/msl-labeled-data-set-v2.1/images/"

    # initialize class names(from class_map.csv file provided with the dataset)
    classes = {
        "0": "Arm cover",
        "1": "Other rover part",
        "2": "Artifact",
        "3": "Nearby surface",    
        "4":	"Close-up rock",
        "5":	"DRT",
        "6":	"DRT spot",
        "7":	"Distant landscape",
        "8":	"Drill hole",
        "9":	"Night sky",
      "10":	"Float",
      "11":	"Layers",
      "12":	"Light-toned veins",
      "13":	"Mastcam cal target",
      "14":	"Sand",
      "15":	"Sun",
      "16":	"Wheel",
      "17":	"Wheel joint",
      "18":	"Wheel tracks"
    }

    print("\n[INFO][LAST] loading...")
    # copy train data to train directory
    with open("/content/msl-labeled-data-set-v2.1/train-set-v2.1.txt") as f:
        data = f.read().split("\n")

        for image_label in data:
            path = image_label.split(" ")
            if len(path) > 1:
              image = path[0]
              label = classes[path[-1]]
            
              # define destination folder
              destination = "/content/msl_splitted_data/train/{}/".format(label)
              
              # if destination folder does not exists create a new one
              if not os.path.exists(destination):
                  os.makedirs(destination)
                  
              # copy file
              copyfile(source+image, destination+image)

        print("[INFO] Done...")


    # create validation directory
    with open("/content/msl-labeled-data-set-v2.1/val-set-v2.1.txt") as f:
        data = f.read().split("\n")
        for image_label in data:
            path = image_label.split(" ")
            if len(path) > 1:
              image = path[0]
              label = classes[path[-1]]
            
              # define destination folder
              destination = "/content/msl_splitted_data/validation/{}/".format(label)
              
              # if destination folder does not exists create a new one
              if not os.path.exists(destination):
                  os.makedirs(destination)
                  
              # copy file
              copyfile(source+image, destination+image)

        print("[INFO] Done...")

    # create test directory
    with open("/content/msl-labeled-data-set-v2.1/test-set-v2.1.txt") as f:
        data = f.read().split("\n")

        for image_label in data:
            path = image_label.split(" ")
            if len(path) > 1:
              image = path[0]
              label = classes[path[-1]]

            
              # define destination folder
              destination = "/content/msl_splitted_data/test/{}/".format(label)
              
              # if destination folder does not exists create a new one
              if not os.path.exists(destination):
                  os.makedirs(destination)
                  
              # copy file
              copyfile(source+image, destination+image)

        print("[INFO] Done...")




























