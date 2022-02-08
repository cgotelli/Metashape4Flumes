
function writeRunFile(fid, mainPath, workflowPath, configPath)

% D:\SfM\RAW\runfiles\run.py
if fid == 1

    outfid = fopen(fullfile(mainPath, 'run.py'), 'wt');
    fprintf(outfid, strcat('import os', '\n'));
    fprintf(outfid, strcat('os.system(''python', " ", strrep(workflowPath,"\","/"), " ", strrep(configPath ,"\","/"), '''',')','\n'));
else    
    
    outfid = fopen(fullfile(mainPath, 'run.py'), 'at');
    fprintf(outfid, strcat('os.system(''python', " ", strrep(workflowPath,"\","/"), " ", strrep(configPath ,"\","/") , '''',')','\n'));

end

fclose(outfid);


end

