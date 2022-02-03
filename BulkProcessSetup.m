
imageFormat ='.jpg';
filesPath = uigetdir('C:\Users\EPFL-LHE\Documents\GitHub\Metashape-BulkProcess\photos\100MEDIA', 'Path where matfiles are stored');
filenames = dir(fullfile(filesPath, '*.jpg')); % Gets all the files with *.mat extension inside the folder, and stores the information in a struct-type variable