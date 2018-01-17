function [DS,devicename]=initDaqSession(Duration,SampleRate,Sound)
%Duration = samplingtime per trigger in seconds
%SamplingsRate = integer in Hz,(for NI USB 6211 max 250000/NumCh)
%Sound=1 for sound, 0 for NI USB 6211
%Created from legacy interface version by DKD for session based interface 29.01.2016
% Find out what HW is recognized and store info in daqinfo
daqinfo=daq.getDevices;
% Find the name of the device, Dev1, Dev2, Audio1...
if Sound
    devicename='Audio1';
    %DAQ session object DS created
    DS=daq.createSession('directsound');
else
    %DAQ session object DS created
    DS=daq.createSession('ni');
    for i=1:length(daqinfo)
        a=getfield(daqinfo(1,i),'ID');
        if a(1:3)=='Dev'; devicename=a; end
    end
end
%Set the rate of sampling (in Hz)
DS.Rate=SampleRate;
%Set duration
DS.DurationInSeconds=Duration;
