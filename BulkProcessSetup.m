
imageFormat ='.jpg';
filesPath = uigetdir('C:\Users\cleme\Desktop\photos', 'Path where matfiles are stored');
filenames = dir(fullfile(filesPath, '*.jpg')); % Gets all the files with *.mat extension inside the folder, and stores the information in a struct-type variable

%%

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
