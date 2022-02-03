% This function prepares the photos for the Metashape automatized process.
% It changes the names to fit the ones established in the script.
% As in the flume we have 104 photos (52 from each camera). These photos 
% are taken always in the same positions, so on each survey the markers 
% appear in the same correlative position. The idea is to have the markers
% always in pictures with the same name. This way we don't have to change 
% the main code for each survey. It's easier to change the names of the
% pictures each time with this script.
%
% The code works as follows:
% * In one folder we have to create one subfolder per survey. At the end of
% a day where we scanned 5 times the bed, we should have 5 subfolders
% inside the main directory.
% * Then, we run this script and we choose the path of the main folder.
% * The code will enter each subfolder, changing the names of all the
% pictures inside. If the photo-capturing process is correct, we should
% have the same amount of pictures inside each subfolder. At the same time,
% each photo with the same name should be a photo taken from the same spot.
% Thus, photos with the same name should show the same markers.

% Parameters for processing
originalPath = pwd;
filesPath = uigetdir('C:\Users\cleme\Desktop\photos', 'Path where matfiles are stored'); % We choose the main folder path using the GUI
content = dir(filesPath);
dfolders = content([content(:).isdir]);
dfolders = dfolders(~ismember({dfolders(:).name},{'.','..'})); % From the content inside the main folder we keep only the path of subfolders


%% Renaming process

% For each subfolder we enter and change the name of the files inside
for fid = 1 :length(dfolders)

    disp(strcat("Working on folder: ", dfolders(fid).name))

    cd(fullfile(dfolders(fid).folder, dfolders(fid).name))
    
    filenames = dir(fullfile('*.jpg')); 
    
    for id = 1:length(filenames)

        f = filenames(id).name;

        disp(f)

        if strcmp(f(1:3), 'LFT')

            if ~strcmp(f, strcat('LFT_', sprintf('%03d.jpg', id)))

                movefile(fullfile(filenames(id).folder, f), fullfile(filenames(id).folder, strcat('LFT_', sprintf('%03d.jpg', id))));

            else

                disp('Did not modify the name')

            end

        elseif strcmp(f(1:3), 'RGT')

            if ~strcmp(f, strcat('RGT_', sprintf('%03d.jpg', id)))

                movefile(fullfile(filenames(id).folder, f), fullfile(filenames(id).folder, strcat('RGT_', sprintf('%03d.jpg', id))));

            else

                disp('Did not modify the name')

            end

        else

            disp('Did not modify the name')

        end

    end

end

% We come back to the original folder
cd(originalPath)
