function writeConfig(filein, fileout, subfolder, photoPath, outputPath, projectPath)
%WRITECONFIG Summary of this function goes here
%   Detailed explanation goes here
% fileID_in = fileread('D:\SfM\RAW\config_common\halle_config_working.yml');
% fileID_out = fopen('config.txt','w');

infid = fopen(filein, 'rt');
outfid = fopen(fileout, 'wt');
i = 1;
while true
    if i == 1
        fprintf(outfid, strcat("main_path: ", '"', strrep(photoPath,"\","/"), '"' ,'\n'));  %the text you are adding at the beginning
        
        i = i+1;
    elseif i == 2
        fprintf(outfid, strcat("subFolder: ", '"', subfolder, '"', '\n') );  %the text you are adding at the beginning\
        i = i+1;
    elseif i == 3
        fprintf(outfid, strcat("output_path: ", '"', strrep(outputPath,"\","/"), '"', '\n') );  %the text you are adding at the beginning\
        i = i+1;
    elseif i == 4
        fprintf(outfid, strcat("project_path: ", '"', strrep(projectPath,"\","/"), '"', '\n') );  %the text you are adding at the beginning\
        i = i+1;
    else
        thisline = fgetl(infid);    %read line from input file
        i = i+1;
        if ~ischar(thisline); break; end    %reached end of file
        fprintf( outfid, '%s\n', thisline );   %write the line to the output file
    end
end
fclose(infid);
fclose(outfid);
end

