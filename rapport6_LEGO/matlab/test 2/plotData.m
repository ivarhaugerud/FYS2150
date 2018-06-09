function plotData(src, event)
    global zeroVoltage
    figure(1),hold on 
    %plot(mean(event.TimeStamps), mean(event.Data(:,1)), 'o', 'color', 'r')
    plot(mean(event.TimeStamps), mean(event.Data(:,2))-zeroVoltage, 'x', 'color', 'b')
    % figure(2),hold on 
    % plot(mean(event.Data(:,1)), mean(event.Data(:,2)),'o')
end