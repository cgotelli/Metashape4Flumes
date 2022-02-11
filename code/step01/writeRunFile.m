
function writeRunFile(fid, workflow, workflowPyPath, configPath)

% D:\SfM\CODE\step02\run.py
if fid == 1

    outfid = fopen(fullfile(workflowPath, 'run.py'), 'wt');
    fprintf(outfid, strcat('import os', '\n'));
    fprintf(outfid, strcat('os.system(''python', " ", strrep(workflowPyPath,"\","/"), " ", strrep(configPath ,"\","/"), '''',')','\n'));
else    
    
    outfid = fopen(fullfile(workflowPath, 'run.py'), 'at');
    fprintf(outfid, strcat('os.system(''python', " ", strrep(workflowPyPath,"\","/"), " ", strrep(configPath ,"\","/") , '''',')','\n'));

end

fclose(outfid);


end

