filePaths = {'/project/6053072/jtang1/jt_unlist/lymph-piq-withBkg/LIST0000.BLF', '/project/6053072/jtang1/jt_unlist/lymph-piq-withBkg/LIST0001.BLF'}

% Energy mode unlisting (if energy-mode list-file)
rx.listmodeWithEnergyFlag = 0; % Set = 1 if want to use energy limits below (default is 425 to 650 keV)
rx.lowEnergyLim = 425; % [keV]
rx.highEnergyLim = 650; % [keV]

% Unlist parameters
rx.tofMode = 'tof'; % Options: nontof, tof
rx.unlistType = 'static'; % Options: static, dynamic, gated
rx.startMsecVec = 0; % Unlist 5 minutes into 1 frame [msec]
scan_duration = [1 2 5 10]*60*1000; % array elements in minutes, convert to ms
for t = scan_duration
    rx.endMsecVec = t;
    for i = 1:length(filePaths)
        t
        filePath = filePaths{i}
        rx.listFilePath = filePath;
        % Call main function
        data = UnlistMain(rx);
    end
end
