function [AIch]=initADchannel(DS,devicename,NumCh,TerminalConfig,Amplitude)
%DAQ session object DS created function initDaqSession
%NumCh = integer, number of channels
%TerminalConfig = 'Differential' (between two channels) or 'SingleEnded'
%           (referenced to ground)
%Amplitude = number, Measurement range +/- 0.2, 1, 5, 10 V
%Created from legacy interface version by DKD for session based interface 20.01.2016
%Changelog: 25.01.2016: Syntaksen for Range og TerminalConfig av flere
%           kanaler måtte endres
%Analog Input channel specific parameters
%Add channels to read
AIch=addAnalogInputChannel(DS,devicename,0:NumCh-1,'Voltage');
for i=1:NumCh
    %Set voltage range/ amplitude
    AIch(i).Range=[-Amplitude Amplitude];
    %Set whether SingleEnded or Differential measurements are to be performed
    AIch(i).TerminalConfig=TerminalConfig;
end
