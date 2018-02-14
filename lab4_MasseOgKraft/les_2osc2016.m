%**************************************************************************
% les_osc.m
%**************************************************************************
% bruke DAQ-kortet som oscilloskop med 2 kanaler for øvelsen Masse og kraft
% Spenning leses på AI0+/- (Ve, utgang fra broen) og AI1+/- (VE, påtrykt)
%**************************************************************************

clear all
close all

datafreq = 10;%frekvens på den påtrykte spenningen
amplitude = 5.0; %hvor stor amplityder kan leses inn
varighet = 10; %sekunder
SampleRate=1000; % Hz

%%%%%%%%%%%%%%%%% Initialisere AD-omformingen til input: AI %%%%%%%%%%%
[DS,devicename]=initDaqSession(varighet,SampleRate,0);
[AI]=initADchannel(DS,devicename,2,'Differential',amplitude);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% Start måling (med AD) %%%
[datain, time] = startForeground(DS);
%%% Vis den målte spenningen som funksjon av tid %%%
Vbro = datain(1:end,1);
VE = datain(1:end,2);
figure(1), hold on;
plot(time,VE,'r');
plot(time,100.*Vbro,'b');
legend('Input V_E','Output V_e*100')
xlabel('t [sec]')
ylabel('Spenning [V]')
hold off

%Filtrering skal dere kunne legge til her

