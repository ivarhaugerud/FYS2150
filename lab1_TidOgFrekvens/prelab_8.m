N = 5

for j=1:N

n = 10^j
a = 3;
b = 2;
x = a+b*randn(1,n);
xmid = mean(x)
s =  mean(x)
sm = s/sqrt(n)

figure(1),clf
plot(x,'k.'), xlabel('Maaling-nummer'),ylabel('x')

hold on

line([0 n],[xmid xmid],'Color','k','LineStyle','-')
line([0 n],[xmid-s xmid-s],'Color','k','LineStyle','--')
line([0 n],[xmid+s xmid+s],'Color','k','LineStyle','--')
line([0 n],[xmid-sm xmid-sm],'Color','k','LineStyle',':')
line([0 n],[xmid+sm xmid+sm],'Color','k','LineStyle',':')
title(['Syntetisk datasett med ',num2str(n),' maalinger'])
text(10,xmid-s-.5,'-ett standardavvik')
text(10,xmid+s+.5,'+ett standardavvik')
text(10,xmid+sm+.5,'+ett standardavvik til middelverdien')
text(10,xmid-sm-.5,'-ett standardavvik til middelverdien')
hold off
end