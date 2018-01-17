%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Program for å lese inn pulser fra fotodiode 
% og måle perioden til signalet
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% Initialiser %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
duration = 1; % antall sekunder vi skal måle
samplerate=25e3;  % vil lese inn data med 25kHz
channel=1; % Antall kanaler på dataloggeren, starter fra 0
inputrange=10; % innspenning mellom -10 og 10 volt
%Create a session
[DS,devicename]=initDaqSession(duration,samplerate,0);
%Initialize the analog input
[AIch]=initADchannel(DS,devicename,1,'SingleEnded',inputrange);
global data time risingEdge periods meanperiod stdofmeanperiod
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Gjør målingene nå
[data time] = startForeground(DS);
%%%% Analyser data %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Finn rising edge (der verdiene stiger) ved å sammenligne hvert datapunkt
% med det etterfølgende datapunktet
threshold = 3.5; %Sett spenningen der passering noteres
risingEdge = find(data(1:end-1) < threshold & data(2:end) > threshold);
% Finn perioden til signalet
periods=diff(time(risingEdge(2:2:end))); %finn tid mellom annenhver risingEdge
meanperiod=mean(periods)
stdofmeanperiod=std(periods)/sqrt(length(periods))
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%% Plott data %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure(1),plot(time, data), hold on
plot(time(risingEdge(2:end-1)),threshold*ones(1,...
    length(risingEdge(2:end-1))),'o'), hold off
xlabel('tid (s)'),ylabel('spenning (V)')
figure(2), plot(time(risingEdge(2:2:end-2)),periods,'*')
xlabel('tid (s)'),ylabel('periode (s)')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%% Lagre data %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
filename = input('Hvilket filnavn vil du bruke for å lagre dataene?','s');
save(filename,'data','risingEdge','periods','meanperiod','stdofmeanperiod')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
