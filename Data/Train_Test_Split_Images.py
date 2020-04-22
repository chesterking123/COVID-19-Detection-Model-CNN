import os, random, shutil

def copy_files(train_images, test_images, source):
    if not os.path.exists("Training Data"):
        os.mkdir("Training Data")
        training_data_initial = 0
        for image in train_images:
            image = source+"/"+image
            shutil.copy(image, "Training Data")
    else:
        training_data_initial = len(os.listdir("Training Data"))
        for image in train_images:
            image = source+"/"+image
            shutil.copy(image, "Training Data")
        
    if not os.path.exists("Testing Data"):
        os.mkdir("Testing Data")
        testing_data_initial = 0
        for image in test_images:
            image = source+"/"+image
            shutil.copy(image, "Testing Data")
    else:
        testing_data_initial = len(os.listdir("Testing Data"))
        for image in test_images:
            image = source+"/"+image
            shutil.copy(image, "Testing Data")
            
    train_files_tranferred = len(os.listdir("Training Data")) - training_data_initial
    test_files_tranferred = len(os.listdir("Testing Data")) - testing_data_initial
    print("Total files transferred : \n Train Files : (", train_files_tranferred, "/", len(train_images), ")\n Test Files : (", test_files_tranferred, "/", len(test_images), ")")
            
            
def train_test_split_images(source, ratio):
    filenames = os.listdir(source)
    number_files = len(filenames)
    train_no = round(number_files*ratio)
    test_no = number_files - train_no
    train_files = set()
    test_files = set()
    while len(train_files) < train_no:
        train_files.add(random.choice(filenames))
    while len(test_files) < test_no:
        test_files.add(random.choice(filenames))
        
    copy_files(train_files, test_files, source)